# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
from django.db import models
from model_utils.managers import InheritanceManager

# -- own --

# -- code --
class Collection(models.Model):
    id    = models.AutoField(primary_key=True, verbose_name='ID', help_text='ID')
    sku   = models.CharField(max_length=50, unique=True, verbose_name="SKU", help_text="SKU")
    name  = models.CharField(max_length=50, verbose_name="名称", help_text="名称")
    intro = models.TextField(verbose_name="简介", help_text="简介")
    image = models.ImageField(upload_to="build", verbose_name="图片", help_text="图片")

    dummy  = models.BooleanField(default=False, verbose_name="仅占位", help_text="仅占位")
    hidden = models.BooleanField(default=False, verbose_name="隐藏", help_text="隐藏")
    sort   = models.IntegerField(default=0, verbose_name="排序", help_text="排序")

    objects = InheritanceManager()

    class Meta:
        verbose_name = "集合"
        verbose_name_plural = verbose_name
        ordering = ('sort', 'id')


class Build(Collection):

    class Meta:
        verbose_name = "构筑"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Episode(Collection):

    class Meta:
        verbose_name = "卡包"
        verbose_name_plural = verbose_name
        ordering = ('sort', 'id')

    def __str__(self):
        return self.name


class Illustrator(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID", help_text="ID")
    name = models.CharField(max_length=50, verbose_name="名字", help_text="名字")

    class Meta:
        verbose_name = "画师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Rarity(models.TextChoices):
    UC  = "UC", "UC"
    C   = "C", "C"
    N   = "N", "N"
    R   = "R", "R"
    SR  = "SR", "SR"
    SSR = "SSR", "SSR"
    ST  = "ST", "ST"
    S   = "S", "S"
    SP  = "SP", "SP"


class Card(models.Model):
    id    = models.AutoField(primary_key=True, verbose_name="ID", help_text="ID")
    sku   = models.CharField(max_length=50, verbose_name="SKU", help_text="SKU")
    title = models.CharField(max_length=50, verbose_name="称号", help_text="称号")
    build = models.ForeignKey(Build, on_delete=models.PROTECT, verbose_name="构筑", help_text="构筑", related_name="cards")

    hidden = models.BooleanField(default=False, verbose_name="隐藏", help_text="隐藏")
    sort   = models.IntegerField(default=0, verbose_name="排序", help_text="排序")

    objects = InheritanceManager()

    class Meta:
        verbose_name = "卡牌"
        verbose_name_plural = verbose_name
        ordering = ('sort', 'id')


class Character(Card):

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'「{self.title}」{self.build.name}'


class SkillType(models.TextChoices):
    SUPPORT = "SUPPORT", "SUPPORT"
    CENTER  = "CENTER", "CENTER"
    HYPER   = "HYPER", "HYPER"


class Skill(models.Model):
    id          = models.AutoField(primary_key=True, verbose_name="ID", help_text="ID")
    character   = models.ForeignKey(Character, on_delete=models.CASCADE, verbose_name="角色", help_text="角色", related_name="skills")
    type        = models.CharField(max_length=50, verbose_name="类型", help_text="类型", choices=SkillType.choices)
    name        = models.CharField(max_length=50, verbose_name="名字", help_text="名字")
    description = models.TextField(verbose_name="描述", help_text="描述")

    hidden = models.BooleanField(default=False, verbose_name="隐藏", help_text="隐藏")
    sort   = models.IntegerField(default=0, verbose_name="排序", help_text="排序")

    class Meta:
        verbose_name = "角色技能"
        verbose_name_plural = verbose_name
        ordering = ('sort', 'id')

    def __str__(self):
        return f'{self.character.build.name}「{self.character.title}」 {self.type}: {self.name}'


class Trait(models.Model):
    id          = models.AutoField(primary_key=True, verbose_name="ID", help_text="ID")
    name        = models.CharField(max_length=50, verbose_name="名字", help_text="名字")
    description = models.TextField(verbose_name="描述", help_text="描述")
    bgcolor     = models.CharField(max_length=50, verbose_name="背景色", help_text="背景色")

    class Meta:
        verbose_name = "符卡特性"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Type(models.Model):
    id          = models.AutoField(primary_key=True, verbose_name="ID", help_text="ID")
    name        = models.CharField(max_length=50, verbose_name="名字", help_text="名字")
    description = models.TextField(verbose_name="描述", help_text="描述")
    bgcolor     = models.CharField(max_length=50, verbose_name="背景色", help_text="背景色")
    is_attack   = models.BooleanField(default=False, verbose_name="战斗符卡类型？", help_text="战斗符卡类型？")

    class Meta:
        verbose_name = "符卡类型"
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.is_attack:
            return f'战斗符卡/{self.name}'
        else:
            return self.name


class BasicConstraint(models.TextChoices):
    SUPPORT   = "SUPPORT", "SUPPORT"
    CENTER    = "CENTER", "CENTER"
    HYPER     = "HYPER", "HYPER"
    EXCLUSIVE = "EXCLUSIVE", "EXCLUSIVE"


class Spellcard(Card):
    type         = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name="类型", help_text="类型", related_name="spellcards")
    gorgeousness = models.IntegerField(default=0, verbose_name="华丽度", help_text="华丽度")
    cost         = models.IntegerField(default=0, verbose_name="消耗", help_text="消耗")
    effect       = models.TextField(verbose_name="效果", help_text="效果")
    intensity    = models.IntegerField(default=0, verbose_name="强度", help_text="强度")
    traits       = models.ManyToManyField(Trait, verbose_name="特性", help_text="特性", related_name="spellcards", blank=True)
    faq          = models.TextField(verbose_name="FAQ", help_text="FAQ", blank=True)

    basic_constraint = models.CharField(max_length=50, verbose_name="基本约束", help_text="基本约束", choices=BasicConstraint.choices)

    class Meta:
        verbose_name = "符卡"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.build.name} - {self.title}'


class ExtendedConstraint(models.Model):

    id        = models.AutoField(primary_key=True, verbose_name="ID", help_text="ID")
    spellcard = models.ForeignKey(Spellcard, on_delete=models.CASCADE, verbose_name="符卡", help_text="符卡", related_name="extended_constraints")
    type      = models.CharField(max_length=50, verbose_name="类型", help_text="类型")
    effect    = models.CharField(max_length=50, verbose_name="效果", help_text="效果")
    sort      = models.IntegerField(default=0, verbose_name="排序", help_text="排序")

    class Meta:
        verbose_name = "符卡扩展限制"
        verbose_name_plural = verbose_name
        ordering = ('sort', 'id')

    def __str__(self):
        return f'{self.spellcard} - {self.type} - {self.effect}'


class Version(models.Model):
    id          = models.AutoField(primary_key=True, verbose_name="ID", help_text="ID")
    card        = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name="卡牌", help_text="卡牌", related_name="versions")
    version     = models.CharField(max_length=50, verbose_name="版本", help_text="版本", default="经典")
    rarity      = models.CharField(max_length=50, verbose_name="稀有度", help_text="稀有度", choices=Rarity.choices)
    episode     = models.ForeignKey(Episode, on_delete=models.CASCADE, verbose_name="卡包", help_text="卡包", blank=True, null=True, related_name="versions")
    line        = models.CharField(max_length=200, verbose_name="牌语", help_text="牌语")
    illustrator = models.ForeignKey(Illustrator, on_delete=models.PROTECT, verbose_name="画师", help_text="画师", related_name="spellcards")
    image       = models.ImageField(upload_to="card", verbose_name="立绘", help_text="立绘")

    hidden = models.BooleanField(default=False, verbose_name="隐藏", help_text="隐藏")
    sort   = models.IntegerField(default=0, verbose_name="排序", help_text="排序")

    class Meta:
        verbose_name = "卡牌版本"
        verbose_name_plural = verbose_name
        unique_together = [('card', 'version')]
        ordering = ('sort', 'id')

    def __str__(self):
        return f'{self.card} - {self.version} [{self.rarity}]'
