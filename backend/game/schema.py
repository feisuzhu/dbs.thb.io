# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType
import graphene as gh

# -- own --
from . import models


# -- code --
class GameQueryMixin:

    @staticmethod
    def get_queryset(qs, info):
        model = info.parent_type.graphene_type._meta.model
        return models.annotate_qs(model, qs)


class Build(GameQueryMixin, DjangoObjectType):

    class Meta:
        model = models.Build


class Illustrator(GameQueryMixin, DjangoObjectType):
    class Meta:
        model = models.Illustrator


class Character(GameQueryMixin, DjangoObjectType):
    class Meta:
        model = models.Character


class CharacterSkill(GameQueryMixin, DjangoObjectType):
    class Meta:
        model = models.CharacterSkill


class CharacterVersion(GameQueryMixin, DjangoObjectType):
    class Meta:
        model = models.CharacterVersion


class Episode(GameQueryMixin, DjangoObjectType):
    class Meta:
        model = models.Episode


class Trait(GameQueryMixin, DjangoObjectType):
    class Meta:
        model = models.Trait


class Type(GameQueryMixin, DjangoObjectType):
    class Meta:
        model = models.Type


class ExtendedConstraint(GameQueryMixin, DjangoObjectType):
    class Meta:
        model = models.ExtendedConstraint


class Spellcard(GameQueryMixin, DjangoObjectType):
    class Meta:
        model = models.Spellcard


class GameQuery(gh.ObjectType):
    builds = gh.List(gh.NonNull(Build), description='构筑列表', required=True)

    def resolve_builds(self, info):
        return models.Build.objects.all().order_by('sort', 'id')

    episodes = gh.List(gh.NonNull(Episode), description='卡包列表', required=True)

    def resolve_episodes(self, info):
        return models.Episode.objects.all().order_by('sort', 'id')
