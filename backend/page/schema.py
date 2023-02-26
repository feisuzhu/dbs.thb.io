# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType
import graphene as gh

# -- own --
from . import models


# -- code --
class ArticleCategory(DjangoObjectType):

    class Meta:
        model = models.ArticleCategory

    articles = gh.List(gh.NonNull('page.schema.Article'), required=True, description="文章列表", reverse=gh.Boolean(default_value=False))

    @staticmethod
    def resolve_articles(root, info, reverse):
        rev = '-' if reverse else ''
        qs = root.articles.order_by(f'{rev}created_at')
        return qs

    article = gh.Field('page.schema.Article', slug=gh.String(required=True), description="文章")

    @staticmethod
    def resolve_article(root, info, slug):
        return root.articles.filter(slug=slug).first()


class Article(DjangoObjectType):

    class Meta:
        model = models.Article


class InfoBlock(DjangoObjectType):

    class Meta:
        model = models.InfoBlock


class InfoBlockButton(DjangoObjectType):

    class Meta:
        model = models.InfoBlockButton


class Landing(DjangoObjectType):

    class Meta:
        model = models.Landing

    def resolve_columns(self, info):
        return self.columns.order_by('sort')

    def resolve_slides(self, info):
        return self.slides.order_by('sort')


class LandingWorks(DjangoObjectType):

    class Meta:
        model = models.LandingWork


class LandingColumn(DjangoObjectType):

    class Meta:
        model = models.LandingColumn


class LandingSlide(DjangoObjectType):

    class Meta:
        model = models.LandingSlide


class OutboundLink(DjangoObjectType):

    class Meta:
        model = models.OutboundLink


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


@staticmethod
def universal_get(root, info, **kwargs):
    ty, got_list = strip_ty(info.return_type)
    model = ty.graphene_type._meta.model

    qs = model.objects.filter(**kwargs)
    if hasattr(qs.model, 'hidden'):
        qs = qs.filter(hidden=False)

    if not got_list:
        qs = qs.first()

    return qs


class PageQuery(gh.ObjectType):

    landing = gh.Field(Landing, required=True, description="首页", resolver=universal_get)
    outbound_links = gh.List(gh.NonNull(OutboundLink), required=True, description="外链列表", resolver=universal_get)

    articles = gh.List(gh.NonNull(Article), required=True, description="文章列表", reverse=gh.Boolean(default_value=False))

    def resolve_articles(self, info, reverse):
        rev = '-' if reverse else ''
        qs = models.Article.objects.filter(category__hidden=False).order_by(f'{rev}created_at')
        return qs

    article_category = gh.Field(ArticleCategory, slug=gh.String(required=True), description="文章分类")

    @staticmethod
    def resolve_article_category(root, info, slug):
        return models.ArticleCategory.objects.filter(slug=slug).first()

    article_categories = gh.List(gh.NonNull(ArticleCategory), required=True, description="文章分类列表", resolver=universal_get)

    info_blocks = gh.List(
        gh.NonNull(InfoBlock),
        required=True,
        description="信息块列表",
        category=gh.Enum.from_enum(models.InfoBlockCategory)(required=True),
        resolver=universal_get,
    )
