# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType
import graphene as gh

# -- own --
from . import models


# -- code --
class Build(DjangoObjectType):
    class Meta:
        model = models.Build


class Illustrator(DjangoObjectType):
    class Meta:
        model = models.Illustrator


class Character(DjangoObjectType):
    class Meta:
        model = models.Character


class CharacterSkill(DjangoObjectType):
    class Meta:
        model = models.CharacterSkill


class CharacterVersion(DjangoObjectType):
    class Meta:
        model = models.CharacterVersion


class Episode(DjangoObjectType):
    class Meta:
        model = models.Episode


class Trait(DjangoObjectType):
    class Meta:
        model = models.Trait


class Type(DjangoObjectType):
    class Meta:
        model = models.Type


class ExtendedConstraint(DjangoObjectType):
    class Meta:
        model = models.ExtendedConstraint


class Spellcard(DjangoObjectType):
    class Meta:
        model = models.Spellcard


class GameQuery(gh.ObjectType):
    episodes = gh.List(gh.NonNull(Episode), description='卡包列表', required=True)

    def resolve_episodes(self, info):
        return models.Episode.objects.all().order_by('sort', 'id')
