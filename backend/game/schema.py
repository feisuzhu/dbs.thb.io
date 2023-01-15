# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType
import graphene as gh

# -- own --
from . import models


# -- code --
class FilteringMixin:

    @staticmethod
    def get_queryset(qs, info):
        model = info.parent_type.graphene_type._meta.model
        return models.annotate_qs(model, qs)


def Navigation(clsname):

    @staticmethod
    def resolve_prev(root, info):
        return root._meta.model.objects.order_by('-id').filter(state='NORMAL', id__lt=root.id).first()

    @staticmethod
    def resolve_next(root, info):
        return root._meta.model.objects.order_by('id').filter(state='NORMAL', id__gt=root.id).first()

    return type(f'{clsname}Navigation', (object,), {
        'prev': gh.Field(f'game.schema.{clsname}', description='上一个'),
        'resolve_prev': resolve_prev,
        'next': gh.Field(f'game.schema.{clsname}', description='下一个'),
        'resolve_next': resolve_next,
    })



class Build(Navigation('Build'), FilteringMixin, DjangoObjectType):

    class Meta:
        model = models.Build


class Illustrator(FilteringMixin, DjangoObjectType):
    class Meta:
        model = models.Illustrator


class Character(Navigation('Character'), FilteringMixin, DjangoObjectType):
    class Meta:
        model = models.Character


class CharacterSkill(FilteringMixin, DjangoObjectType):
    class Meta:
        model = models.CharacterSkill


class CharacterVersion(FilteringMixin, DjangoObjectType):
    class Meta:
        model = models.CharacterVersion


class Episode(Navigation('Episode'), FilteringMixin, DjangoObjectType):
    class Meta:
        model = models.Episode


class Trait(FilteringMixin, DjangoObjectType):
    class Meta:
        model = models.Trait


class Type(FilteringMixin, DjangoObjectType):
    class Meta:
        model = models.Type


class ExtendedConstraint(FilteringMixin, DjangoObjectType):
    class Meta:
        model = models.ExtendedConstraint


class Spellcard(Navigation('Spellcard'), FilteringMixin, DjangoObjectType):
    class Meta:
        model = models.Spellcard


class GameQuery(gh.ObjectType):
    builds = gh.List(gh.NonNull(Build), description='构筑列表', required=True)

    def resolve_builds(self, info):
        return models.Build.objects.all().order_by('sort', 'id')

    build = gh.Field(Build, sku=gh.String(required=True, description="SKU"), description='构筑')

    def resolve_build(self, info, sku):
        return models.Build.objects.get(sku=sku)

    episodes = gh.List(gh.NonNull(Episode), description='卡包列表', required=True)

    def resolve_episodes(self, info):
        return models.Episode.objects.all().order_by('sort', 'id')

    episode = gh.Field(Episode, sku=gh.String(required=True, description="SKU"), description='卡包')

    def resolve_episode(self, info, sku):
        return models.Episode.objects.get(sku=sku)
