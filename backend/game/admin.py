from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


def make_hidden(modeladmin, request, queryset):
    """设置选中的项目为隐藏状态"""
    updated = queryset.update(hidden=True)
    modeladmin.message_user(request, f'成功设置 {updated} 个项目为隐藏状态。')
make_hidden.short_description = "设置成隐藏"


def make_visible(modeladmin, request, queryset):
    """取消选中项目的隐藏状态"""
    updated = queryset.update(hidden=False)
    modeladmin.message_user(request, f'成功取消 {updated} 个项目的隐藏状态。')
make_visible.short_description = "取消隐藏"


# class Build(models.Model):
@admin.register(models.Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'name', 'dummy', 'hidden', 'sort')
    list_filter = ('hidden', 'dummy')
    search_fields = ('name', 'version')
    ordering = ('sort',)
    sort_order = 20
    actions = [make_hidden, make_visible]

# class Illustrator(models.Model):
@admin.register(models.Illustrator)
class IllustratorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ()
    search_fields = ('name',)
    ordering = ('name',)


# class Skill(models.Model):
class SkillInline(admin.TabularInline):
    model = models.Skill
    extra = 1


# class SpellcardVersion(models.Model):
class VersionInline(admin.TabularInline):
    model = models.Version
    extra = 1


# class Character(models.Model):
@admin.register(models.Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'title', 'build', 'hidden', 'sort')
    list_filter = ('versions__rarity', 'versions__illustrator', 'build', 'hidden')
    search_fields = ('title', 'versions__illustrator', 'build', 'faq')
    inlines = [VersionInline, SkillInline]
    ordering = ('sort',)
    sort_order = 15
    actions = [make_hidden, make_visible]

    fieldsets = (
        ('角色', {
            'fields': (('sku', 'hidden', 'sort'), ('title', 'build'))
        }),
    )


# class Episode(models.Model):
@admin.register(models.Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'name', 'image', 'dummy', 'hidden', 'sort')
    list_filter = ('hidden', 'dummy')
    filter_horizontal = ('versions',)
    search_fields = ('sku', 'name', 'intro')
    ordering = ('sort',)
    sort_order = 40
    actions = [make_hidden, make_visible]


# class Collection(models.Model):
class CollectionAdmin(admin.ModelAdmin):
    pass

# class Trait(models.Model):
@admin.register(models.Trait)
class TraitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ()
    search_fields = ()
    ordering = ('name',)
    sort_order = 60


# class Type(models.Model):
@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_attack')
    list_filter = ('is_attack',)
    search_fields = ()
    ordering = ('name',)
    sort_order = 50

class ExtendedConstraintInline(admin.TabularInline):
    model = models.ExtendedConstraint
    extra = 1


# class Spellcard(models.Model):
@admin.register(models.Spellcard)
class SpellcardAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'build', 'title', 'type', 'gorgeousness', 'basic_constraint', 'has_extended_constraint', 'hidden', 'sort')
    list_filter = ('build', 'type', 'gorgeousness', 'versions__illustrator', 'versions__rarity', 'versions__episodes', 'traits__name', 'hidden')
    search_fields = ('title', 'effect', 'faq')
    filter_horizontal = ('traits',)
    ordering = ('sort',)
    inlines = [ExtendedConstraintInline, VersionInline]
    actions = [make_hidden, make_visible]

    sort_order = 10

    fieldsets = (
        ('编制 & 描述', {
            'fields': (('sku', 'hidden', 'sort'), ('title', 'build'))
        }),
        ('游戏', {
            'fields': (('type', 'cost', 'lsc', 'intensity'), ('basic_constraint', 'gorgeousness'), 'traits', 'effect', 'faq')
        }),
    )

    def has_extended_constraint(self, obj):
        return obj.extended_constraints.exists()

    has_extended_constraint.boolean = True
    has_extended_constraint.short_description = '有额外限制？'


# 为 Skill 模型添加 admin
@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'character', 'type', 'name', 'hidden', 'sort')
    list_filter = ('type', 'hidden', 'character__build')
    search_fields = ('name', 'description', 'character__title')
    ordering = ('sort',)
    actions = [make_hidden, make_visible]


# 为 Version 模型添加 admin
@admin.register(models.Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'card', 'version', 'rarity', 'illustrator', 'hidden', 'sort')
    list_filter = ('rarity', 'hidden', 'illustrator', 'card__build')
    search_fields = ('card__title', 'version', 'line', 'illustrator__name')
    ordering = ('card__sort', 'sort')
    actions = [make_hidden, make_visible]
