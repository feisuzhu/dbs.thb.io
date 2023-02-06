# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType
import graphene as gh

# -- own --
from . import models


# -- code --
def strip_ty(ty):
    got_list = False
    while True:
        if ty.__class__.__name__ == 'GraphQLNonNull':
            ty = ty.of_type
        elif ty.__class__.__name__ == 'GraphQLList':
            ty = ty.of_type
            got_list = True
        else:
            return ty, got_list


def annotate_qs(qs, info):
    ty = info.return_type
    ty, got_list = strip_ty(ty)
    model = ty.graphene_type._meta.model

    if hasattr(model, 'hidden'):
        qs = qs.filter(hidden=False)
    if hasattr(model, 'dummy') and not got_list:
        qs = qs.filter(dummy=False)

    return qs


class Filtering:
    @classmethod
    def __init_subclass_with_meta__(cls, model=None, exclude=None, **options):
        assert model is not None, 'model is required'

        @staticmethod
        def get_queryset(qs, info):
            return annotate_qs(qs, info)

        cls.get_queryset = get_queryset
        exclude = exclude or []
        exclude.append('hidden')

        super(Filtering, cls).__init_subclass_with_meta__(
            model=model, exclude=exclude, **options,
        )


class Navigation:
    @classmethod
    def __init_subclass_with_meta__(cls, model=None, **options):
        assert model is not None, 'model is required'

        filters = {}
        if hasattr(model, 'hidden'):
            filters['hidden'] = False
        if hasattr(model, 'dummy'):
            filters['dummy'] = False

        def resolve_prev(root, info):
            return model.objects.order_by('-id').filter(**filters, id__lt=root.id).first()

        def resolve_next(root, info):
            return model.objects.order_by('id').filter(**filters, id__gt=root.id).first()

        cls.prev = gh.Field(cls, resolver=resolve_prev, description=f'上一个{model._meta.verbose_name}')
        cls.next = gh.Field(cls, resolver=resolve_next, description=f'下一个{model._meta.verbose_name}')

        super(Navigation, cls).__init_subclass_with_meta__(
            model=model, **options,
        )


class Build(Navigation, Filtering, DjangoObjectType):

    class Meta:
        model = models.Build

    first_entity = gh.Field('game.schema.Card', description='第一个实体卡')

    def resolve_first_entity(self, info):
        entity = self.characters.first() or self.spellcards.first()
        return entity


class Illustrator(DjangoObjectType):
    class Meta:
        model = models.Illustrator


class Character(Navigation, Filtering, DjangoObjectType):
    class Meta:
        model = models.Character


class CharacterSkill(Filtering, DjangoObjectType):
    class Meta:
        model = models.CharacterSkill


class CharacterVersion(Filtering, DjangoObjectType):
    class Meta:
        model = models.CharacterVersion


class Episode(Navigation, Filtering, DjangoObjectType):
    class Meta:
        model = models.Episode

    first_entity = gh.Field('game.schema.Card', description='第一个实体卡')

    def resolve_first_entity(self, info):
        entity = self.characters.first() or self.spellcards.first()
        return entity


class Trait(DjangoObjectType):
    class Meta:
        model = models.Trait


class Type(DjangoObjectType):
    class Meta:
        model = models.Type


class ExtendedConstraint(DjangoObjectType):
    class Meta:
        model = models.ExtendedConstraint


class Version(Filtering, DjangoObjectType):
    class Meta:
        model = models.Version


class Spellcard(Navigation, Filtering, DjangoObjectType):
    class Meta:
        model = models.Spellcard


class Card(gh.Union):
    class Meta:
        types = (Character, Spellcard)


class GameQuery(gh.ObjectType):
    @staticmethod
    def _root_list(root, info, **kwargs):
        ty, got_list = strip_ty(info.return_type)
        assert got_list
        assert root is None
        model = ty.graphene_type._meta.model
        return annotate_qs(model.objects, info)

    @staticmethod
    def _root_get(root, info, **kwargs):
        ty, got_list = strip_ty(info.return_type)
        assert not got_list
        assert root is None
        model = ty.graphene_type._meta.model
        return annotate_qs(model.objects, info).filter(**kwargs).first()

    builds     = gh.List(gh.NonNull(Build), description='构筑列表', required=True, resolver=_root_list)
    build      = gh.Field(Build, sku=gh.String(required=True, description="SKU"), description='构筑', resolver=_root_get)
    episodes   = gh.List(gh.NonNull(Episode), description='卡包列表', required=True, resolver=_root_list)
    episode    = gh.Field(Episode, sku=gh.String(required=True, description="SKU"), description='卡包', resolver=_root_get)

    character = gh.Field(Character, sku=gh.String(required=True, description="SKU"), description='角色', resolver=_root_get)
    spellcard = gh.Field(Spellcard, sku=gh.String(required=True, description="SKU"), description='符卡', resolver=_root_get)
