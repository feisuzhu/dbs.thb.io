# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
from django.db import models
from model_utils.managers import InheritanceManager

# -- own --

# -- code --
_ = lambda s, s1 = None: { 'verbose_name': s, 'help_text': f'{s}（{s1}）' if s1 else s }


class Collection(models.Model):
    id    = models.AutoField(primary_key=True, **_("ID"))
    sku   = models.CharField(max_length=50, unique=True, **_("SKU"))
    name  = models.CharField(max_length=50, **_("名称"))
    intro = models.TextField(**_("简介"))
    image = models.ImageField(upload_to="build", **_("图片", "757x247"))

    dummy  = models.BooleanField(default=False, **_("仅占位"))
    hidden = models.BooleanField(default=False, **_("隐藏"))
    sort   = models.IntegerField(default=0, **_("排序"))

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
    versions = models.ManyToManyField("Version", **_("卡牌版本"), related_name="episodes")

    objects = InheritanceManager()

    class Meta:
        verbose_name = "卡包"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Illustrator(models.Model):
    id = models.AutoField(primary_key=True, **_("ID"))
    name = models.CharField(max_length=50, **_("名字"))

    class Meta:
        verbose_name = "画师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Rarity(models.TextChoices):
    N   = "N", "N"
    R   = "R", "R"
    SR  = "SR", "SR"
    SSR = "SSR", "SSR"
    PR  = "PR", "PR"
    TR  = "TR", "TR"


class Card(models.Model):
    id    = models.AutoField(primary_key=True, **_("ID"))
    sku   = models.CharField(max_length=50, **_("SKU"))
    title = models.CharField(max_length=50, **_("称号"))
    build = models.ForeignKey(Build, on_delete=models.PROTECT, **_("构筑"), related_name="cards")
    faq   = models.TextField(**_("FAQ"), blank=True)

    hidden = models.BooleanField(default=False, **_("隐藏"))
    sort   = models.IntegerField(default=0, **_("排序"))

    objects = InheritanceManager()

    class Meta:
        verbose_name = "卡牌"
        verbose_name_plural = verbose_name
        ordering = ('sort', 'id')

    def __str__(self):
        return f'{self.build.name} - {self.title}'


class Character(Card):

    class Meta:
        verbose_name = "角色卡"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'「{self.title}」{self.build.name}'


class SkillType(models.TextChoices):
    SUPPORT = "SUPPORT", "SUPPORT"
    CENTER  = "CENTER", "CENTER"
    HYPER   = "HYPER", "HYPER"


class Skill(models.Model):
    id          = models.AutoField(primary_key=True, **_("ID"))
    character   = models.ForeignKey(Character, on_delete=models.CASCADE, **_("角色卡"), related_name="skills")
    type        = models.CharField(max_length=50, **_("类型"), choices=SkillType.choices)
    name        = models.CharField(max_length=50, **_("名字"))
    description = models.TextField(**_("描述"))

    hidden = models.BooleanField(default=False, **_("隐藏"))
    sort   = models.IntegerField(default=0, **_("排序"))

    class Meta:
        verbose_name = "角色技能"
        verbose_name_plural = verbose_name
        ordering = ('sort', 'id')

    def __str__(self):
        return f'{self.character.build.name}「{self.character.title}」 {self.type}: {self.name}'


class Trait(models.Model):
    id          = models.AutoField(primary_key=True, **_("ID"))
    name        = models.CharField(max_length=50, **_("名字"))
    description = models.TextField(**_("描述"))
    bgcolor     = models.CharField(max_length=50, **_("背景色"))

    class Meta:
        verbose_name = "符卡特性"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Type(models.Model):
    id          = models.AutoField(primary_key=True, **_("ID"))
    name        = models.CharField(max_length=50, **_("名字"))
    description = models.TextField(**_("描述"))
    bgcolor     = models.CharField(max_length=50, **_("背景色"))
    is_attack   = models.BooleanField(default=False, **_("战斗符卡类型？"))

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
    type         = models.ForeignKey(Type, on_delete=models.PROTECT, **_("类型"), related_name="spellcards")
    gorgeousness = models.IntegerField(default=0, **_("华丽度"))
    cost         = models.IntegerField(default=0, **_("消耗"))
    lsc          = models.BooleanField(default=False, **_("终符"))
    effect       = models.TextField(**_("效果"))
    intensity    = models.IntegerField(default=0, **_("强度"))
    traits       = models.ManyToManyField(Trait, **_("特性"), related_name="spellcards", blank=True)

    basic_constraint = models.CharField(max_length=50, **_("基本约束"), choices=BasicConstraint.choices)

    class Meta:
        verbose_name = "符卡"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.build.name} - {self.title}'


class ExtendedConstraint(models.Model):

    id        = models.AutoField(primary_key=True, **_("ID"))
    spellcard = models.ForeignKey(Spellcard, on_delete=models.CASCADE, **_("符卡"), related_name="extended_constraints")
    type      = models.CharField(max_length=50, **_("类型"))
    effect    = models.CharField(max_length=50, **_("效果"))
    sort      = models.IntegerField(default=0, **_("排序"))

    class Meta:
        verbose_name = "符卡扩展限制"
        verbose_name_plural = verbose_name
        ordering = ('sort', 'id')

    def __str__(self):
        return f'{self.spellcard} - {self.type} - {self.effect}'


class Version(models.Model):
    id          = models.AutoField(primary_key=True, **_("ID"))
    card        = models.ForeignKey(Card, on_delete=models.CASCADE, **_("卡牌"), related_name="versions")
    version     = models.CharField(max_length=50, **_("版本"), default="经典")
    rarity      = models.CharField(max_length=50, **_("稀有度"), choices=Rarity.choices)
    line        = models.CharField(max_length=200, **_("牌语"))
    illustrator = models.ForeignKey(Illustrator, on_delete=models.PROTECT, **_("画师"), related_name="spellcards")
    image       = models.ImageField(upload_to="card", **_("立绘", "630x876"))

    hidden = models.BooleanField(default=False, **_("隐藏"))
    sort   = models.IntegerField(default=0, **_("排序"))

    class Meta:
        verbose_name = "卡牌版本"
        verbose_name_plural = verbose_name
        unique_together = [('card', 'version')]
        ordering = ('card__sort', 'sort', 'id')

    def __str__(self):
        return f'{self.card} - {self.version} [{self.rarity}]'
