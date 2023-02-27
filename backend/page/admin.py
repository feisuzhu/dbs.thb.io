# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
from django.contrib import admin

# -- own --
from . import models


# -- code --
@admin.register(models.ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'name', 'sort', 'hidden')
    list_display_links = ('name',)
    search_fields = ('name',)
    sort_order = 20


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'category', 'title', 'created_at', 'updated_at')
    list_display_links = ('slug',)
    list_filter = ('category',)
    search_fields = ('slug', 'title', 'content')
    sort_order = 20


class InfoBlockButtonInline(admin.TabularInline):
    model = models.InfoBlockButton
    extra = 1


@admin.register(models.InfoBlock)
class InfoBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'type', 'title', 'subtitle', 'sort')
    list_display_links = ('title',)
    list_filter = ('category',)
    search_fields = ('title', 'subtitle', 'description', 'content')
    inlines = [InfoBlockButtonInline]
    sort_order = 40


class LandingColumnInline(admin.TabularInline):
    model = models.LandingColumn
    extra = 1


class LandingSlideInline(admin.TabularInline):
    model = models.LandingSlide
    extra = 1


class LandingWorkInline(admin.TabularInline):
    model = models.LandingWork
    extra = 1


@admin.register(models.Landing)
class LandingAdmin(admin.ModelAdmin):
    inlines = [LandingSlideInline, LandingWorkInline, LandingColumnInline]
    sort_order = 10

    fieldsets = (
        ('首页信息', {
            'fields': (('logo', 'monologo'), 'footer')
        }),
    )


@admin.register(models.OutboundLink)
class OutboundLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'mono', 'url', 'sort')
    sort_order = 50

    fieldsets = (
        (None, {
            'fields': (('name', 'sort'), ('icon', 'mono'), 'url')
        }),
    )
