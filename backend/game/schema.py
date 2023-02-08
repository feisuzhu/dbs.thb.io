# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType
from model_utils.managers import InheritanceQuerySet
import graphene as gh

# -- own --
from . import models


# -- code --

# BIG MESS, because select_subclassses is not available everywhere,
# have to hack it around, losing the advantage of using select_subclasses,
# and leaking abstraction.
# But I'm not tinkering with this anymore, just exhausted.

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


def annotate_qs(qs, preserve_dummy):
    if hasattr(qs.model, 'hidden'):
        qs = qs.filter(hidden=False)

    if hasattr(qs.model, 'dummy') and not preserve_dummy:
        qs = qs.filter(dummy=False)

    if select_subclasses := getattr(qs, 'select_subclasses', None):
        qs = select_subclasses()

    return qs


def to_submodel(root):
    iqs = InheritanceQuerySet()
    obj = root
    for subclass in iqs._get_subclasses_recurse(root.__class__):
        obj = iqs._get_sub_obj_recurse(root, subclass)
        if obj:
            break

    return obj



@staticmethod
def universal_get(root, info, preserve_dummy=None, **kwargs):
    ty, got_list = strip_ty(info.return_type)
    assert root is None
    if ty.__class__.__name__ == 'GrapheneUnionType':
        virt = True
        models = [t.graphene_type._meta.model for t in ty.types]
        bases = {m.__bases__ for m in models}
        assert len(bases) == 1
        model = bases.pop()[0]
    elif ty.__class__.__name__ == 'GrapheneInterfaceType':
        virt = True
        model = ty.graphene_type._meta.model
    else:
        virt = False
        model = ty.graphene_type._meta.model

    preserve_dummy = got_list if preserve_dummy is None else preserve_dummy
    qs = annotate_qs(model.objects, preserve_dummy=preserve_dummy).filter(**kwargs)

    if virt:
        qs = qs.select_subclasses()

    if not got_list:
        qs = qs.first()

    return qs


class Filtering:
    @classmethod
    def __init_subclass_with_meta__(cls, model=None, **options):
        assert model is not None, 'model is required'

        @staticmethod
        def get_queryset(qs, info):
            ty = info.return_type
            ty, got_list = strip_ty(ty)
            return annotate_qs(qs, preserve_dummy=got_list)

        cls.get_queryset = get_queryset

        super(Filtering, cls).__init_subclass_with_meta__(
            model=model, **options,
        )

        cls._meta.fields.pop('hidden', None)


class Navigation:
    @classmethod
    def __init_subclass_with_meta__(cls, model=None, **options):
        type = options.get('type', None)
        assert bool(model) ^ bool(type), 'model or type is required'

        if type:
            model = type._meta.model

        filters = {}
        if hasattr(model, 'hidden'):
            filters['hidden'] = False
        if hasattr(model, 'dummy'):
            filters['dummy'] = False

        select_subclasses = hasattr(cls, 'select_subclasses')

        def resolve_prev(root, info):
            qs = model.objects.order_by('-id').filter(**filters, id__lt=root.id)
            qs = qs.select_subclasses() if select_subclasses else qs
            return qs.first()

        def resolve_next(root, info):
            qs = model.objects.order_by('id').filter(**filters, id__gt=root.id)
            qs = qs.select_subclasses() if select_subclasses else qs
            return qs.first()

        cls.prev = gh.Field(cls, resolver=resolve_prev, description=f'上一个{model._meta.verbose_name}')
        cls.next = gh.Field(cls, resolver=resolve_next, description=f'下一个{model._meta.verbose_name}')

        super(Navigation, cls).__init_subclass_with_meta__(
            model=model, **options,
        )


class DjangoInterfaceType(gh.Interface):

    @classmethod
    def __init_subclass_with_meta__(cls, model=None, _meta=None, **options):
        assert model is not None, 'model is required'

        objtype = type(cls.__name__, (DjangoObjectType,), {
            'Meta': type('Meta', (), {
                'model': model,
                'skip_registry': True,
            }),
        })

        if _meta is None:
            # from graphene.types.interface import InterfaceOptions
            from graphene_django.types import DjangoObjectTypeOptions
            _meta = DjangoObjectTypeOptions(cls)
            _meta.fields = objtype._meta.fields
        else:
            _meta.fields.update(objtype._meta.fields)

        from django.db.models.fields.related_descriptors import ForwardOneToOneDescriptor, ReverseOneToOneDescriptor
        for k in list(_meta.fields):
            try:
                if isinstance(field := getattr(model, k), (ForwardOneToOneDescriptor, ReverseOneToOneDescriptor)):
                    if field.related.model is model:
                        _meta.fields.pop(k)
            except AttributeError:
                pass

        _meta.model = objtype._meta.model
        _meta._type = objtype
        _meta.registry = objtype._meta.registry
        _meta.registry._registry[model] = cls

        super(DjangoInterfaceType, cls).__init_subclass_with_meta__(model=model, _meta=_meta, **options)

    @classmethod
    def resolve_type(cls, root, info):
        obj = to_submodel(root)
        return cls._meta.registry.get_type_for_model(obj.__class__)

    @classmethod
    def get_node(cls, info, id):
        ty = info.return_type
        ty, got_list = strip_ty(ty)
        qs = cls.get_queryset(cls._meta.model.objects, info)
        obj = annotate_qs(qs, preserve_dummy=got_list).get(pk=id)
        return to_submodel(obj)


class Collection(Navigation, Filtering, DjangoInterfaceType):
    class Meta:
        model = models.Collection

    first_card = gh.Field('game.schema.Card', description='第一个卡牌')


class Build(Navigation, Filtering, DjangoObjectType):

    class Meta:
        model = models.Build
        interfaces = (Collection,)
        exclude = ('collection_ptr',)

    @staticmethod
    def resolve_first_card(root, info):
        return to_submodel(annotate_qs(root.cards, False).first())


class Illustrator(DjangoObjectType):
    class Meta:
        model = models.Illustrator


class Card(Navigation, Filtering, DjangoInterfaceType):
    class Meta:
        model = models.Card


class Character(Navigation, Filtering, DjangoObjectType):
    class Meta:
        model = models.Character
        interfaces = (Card,)
        exclude = ('card_ptr',)


class Skill(Filtering, DjangoObjectType):
    class Meta:
        model = models.Skill


class Episode(Navigation, Filtering, DjangoObjectType):
    class Meta:
        model = models.Episode
        interfaces = (Collection,)
        exclude = ('collection_ptr',)

    @staticmethod
    def resolve_first_card(root, info):
        v = annotate_qs(root.versions, False).first()
        v = v and v.card
        return to_submodel(v)


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
        interfaces = (Card,)
        exclude = ('card_ptr',)


class GameQuery(gh.ObjectType):

    collections = gh.List(gh.NonNull(Collection), description='集合列表', required=True, resolver=universal_get)
    collection  = gh.Field(Collection, sku=gh.String(required=True, description="SKU"), description='集合', resolver=universal_get)
    builds      = gh.List(gh.NonNull(Build), description='构筑列表', required=True, resolver=universal_get)
    build       = gh.Field(Build, sku=gh.String(required=True, description="SKU"), description='构筑', resolver=universal_get)
    episodes    = gh.List(gh.NonNull(Episode), description='卡包列表', required=True, resolver=universal_get)
    episode     = gh.Field(Episode, sku=gh.String(required=True, description="SKU"), description='卡包', resolver=universal_get)

    card = gh.Field(Card, sku=gh.String(required=True, description="SKU"), description='卡牌', resolver=universal_get)
    character = gh.Field(Character, sku=gh.String(required=True, description="SKU"), description='角色', resolver=universal_get)
    spellcard = gh.Field(Spellcard, sku=gh.String(required=True, description="SKU"), description='符卡', resolver=universal_get)
