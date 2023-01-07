# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
from graphene_django.types import DjangoObjectType
import graphene as gh

# -- own --
from . import models


# -- code --
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


class LandingColumn(DjangoObjectType):

    class Meta:
        model = models.LandingColumn


class LandingSlide(DjangoObjectType):

    class Meta:
        model = models.LandingSlide


class OutboundLink(DjangoObjectType):

    class Meta:
        model = models.OutboundLink


class Page(DjangoObjectType):

    class Meta:
        model = models.Page


class PageQuery(gh.ObjectType):

    landing = gh.Field(Landing, required=True, description="首页")

    def resolve_landing(self, info):
        return models.Landing.objects.get()

    outbound_links = gh.List(
        gh.NonNull(OutboundLink),
        required=True,
        description="外链列表",
    )

    def resolve_outbound_links(self, info):
        return models.OutboundLink.objects.order_by('sort')

    page = gh.Field(Page, description="页面", slug=gh.String(required=True))

    def resolve_page(self, info, slug):
        return models.Page.objects.filter(slug=slug).first()

    articles = gh.List(
        gh.NonNull(Article),
        required=True,
        description="文章列表",
        category=gh.String(required=True),
        reverse=gh.Boolean(default_value=False),
    )

    def resolve_articles(self, info, category, reverse):
        rev = '-' if reverse else ''
        qs = models.Article.objects.filter(category=category).order_by(f'{rev}created_at')
        return qs

    article_categories = gh.List(
        gh.NonNull(gh.String),
        required=True,
        description="文章分类列表",
    )

    def resolve_article_categories(self, info):
        return models.Article.objects.values_list('category', flat=True).distinct()

    info_blocks = gh.List(
        gh.NonNull(InfoBlock),
        required=True,
        description="信息块列表",
        category=gh.Enum.from_enum(models.InfoBlockCategory)(required=True),
    )

    def resolve_info_blocks(self, info, category):
        return models.InfoBlock.objects.filter(category=category).order_by('sort')
