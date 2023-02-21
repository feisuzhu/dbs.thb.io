from django.contrib import admin

from . import models


# class Build(models.Model):
@admin.register(models.Build)
class BuildAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'name', 'dummy', 'hidden', 'sort')
    list_filter = ()
    search_fields = ('name', 'version')
    ordering = ('sort',)
    sort_order = 20

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

    fieldsets = (
        ('角色', {
            'fields': (('sku', 'hidden', 'sort'), ('title', 'build'))
        }),
    )


# class Episode(models.Model):
@admin.register(models.Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'sku', 'name', 'image', 'dummy', 'hidden', 'sort')
    list_filter = ()
    search_fields = ('sku', 'name', 'intro')
    ordering = ('sort',)
    sort_order = 40


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
    list_filter = ('build', 'type', 'gorgeousness', 'versions__illustrator', 'versions__rarity', 'versions__episode', 'traits__name')
    search_fields = ('title', 'effect', 'faq')
    filter_horizontal = ('traits',)
    ordering = ('sort',)
    inlines = [ExtendedConstraintInline, VersionInline]

    sort_order = 10

    fieldsets = (
        ('编制 & 描述', {
            'fields': (('sku', 'hidden', 'sort'), ('title', 'build'))
        }),
        ('游戏', {
            'fields': (('type', 'cost', 'intensity'), ('basic_constraint', 'gorgeousness'), 'traits', 'effect', 'faq')
        }),
    )

    def has_extended_constraint(self, obj):
        return obj.extended_constraints.exists()

    has_extended_constraint.boolean = True
    has_extended_constraint.short_description = '有额外限制？'
