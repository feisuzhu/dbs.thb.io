# Generated by Django 4.1.4 on 2023-01-07 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Build",
            fields=[
                (
                    "id",
                    models.AutoField(
                        help_text="ID",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sku",
                    models.CharField(
                        help_text="SKU", max_length=50, unique=True, verbose_name="SKU"
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="名称", max_length=50, verbose_name="名称"),
                ),
                ("intro", models.TextField(help_text="简介", verbose_name="简介")),
                (
                    "image",
                    models.ImageField(
                        help_text="图片", upload_to="build", verbose_name="图片"
                    ),
                ),
                (
                    "sort",
                    models.IntegerField(default=0, help_text="排序", verbose_name="排序"),
                ),
            ],
            options={
                "verbose_name": "构筑",
                "verbose_name_plural": "构筑",
            },
        ),
        migrations.CreateModel(
            name="Character",
            fields=[
                (
                    "id",
                    models.AutoField(
                        help_text="ID",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sku",
                    models.CharField(
                        help_text="SKU", max_length=50, verbose_name="SKU"
                    ),
                ),
                (
                    "title",
                    models.CharField(help_text="称号", max_length=50, verbose_name="称号"),
                ),
                (
                    "sort",
                    models.IntegerField(default=0, help_text="排序", verbose_name="排序"),
                ),
                (
                    "build",
                    models.ForeignKey(
                        help_text="构筑",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="characters",
                        to="game.build",
                        verbose_name="构筑",
                    ),
                ),
            ],
            options={
                "verbose_name": "角色",
                "verbose_name_plural": "角色",
            },
        ),
        migrations.CreateModel(
            name="Episode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        help_text="ID",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(help_text="标题", max_length=50, verbose_name="标题"),
                ),
                (
                    "subtitle",
                    models.CharField(
                        help_text="副标题", max_length=50, verbose_name="副标题"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="图片", upload_to="episode", verbose_name="图片"
                    ),
                ),
                ("description", models.TextField(help_text="描述", verbose_name="描述")),
                (
                    "sort",
                    models.IntegerField(default=0, help_text="排序", verbose_name="排序"),
                ),
            ],
            options={
                "verbose_name": "卡包",
                "verbose_name_plural": "卡包",
            },
        ),
        migrations.CreateModel(
            name="Illustrator",
            fields=[
                (
                    "id",
                    models.AutoField(
                        help_text="ID",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="名字", max_length=50, verbose_name="名字"),
                ),
            ],
            options={
                "verbose_name": "画师",
                "verbose_name_plural": "画师",
            },
        ),
        migrations.CreateModel(
            name="Trait",
            fields=[
                (
                    "id",
                    models.AutoField(
                        help_text="ID",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="名字", max_length=50, verbose_name="名字"),
                ),
                ("description", models.TextField(help_text="描述", verbose_name="描述")),
                (
                    "bgcolor",
                    models.CharField(
                        help_text="背景色", max_length=50, verbose_name="背景色"
                    ),
                ),
            ],
            options={
                "verbose_name": "符卡特性",
                "verbose_name_plural": "符卡特性",
            },
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.AutoField(
                        help_text="ID",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="名字", max_length=50, verbose_name="名字"),
                ),
                ("description", models.TextField(help_text="描述", verbose_name="描述")),
                (
                    "bgcolor",
                    models.CharField(
                        help_text="背景色", max_length=50, verbose_name="背景色"
                    ),
                ),
                (
                    "is_attack",
                    models.BooleanField(
                        default=False, help_text="战斗符卡类型？", verbose_name="战斗符卡类型？"
                    ),
                ),
            ],
            options={
                "verbose_name": "符卡类型",
                "verbose_name_plural": "符卡类型",
            },
        ),
        migrations.CreateModel(
            name="Spellcard",
            fields=[
                (
                    "id",
                    models.AutoField(
                        help_text="ID",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sku",
                    models.CharField(
                        help_text="SKU", max_length=50, unique=True, verbose_name="SKU"
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="符卡名", max_length=50, verbose_name="符卡名"
                    ),
                ),
                (
                    "gorgeousness",
                    models.IntegerField(default=0, help_text="华丽度", verbose_name="华丽度"),
                ),
                (
                    "cost",
                    models.IntegerField(default=0, help_text="消耗", verbose_name="消耗"),
                ),
                ("effect", models.TextField(help_text="效果", verbose_name="效果")),
                (
                    "intensity",
                    models.IntegerField(default=0, help_text="强度", verbose_name="强度"),
                ),
                (
                    "faq",
                    models.TextField(blank=True, help_text="FAQ", verbose_name="FAQ"),
                ),
                (
                    "basic_constraint",
                    models.CharField(
                        choices=[
                            ("SUPPORT", "SUPPORT"),
                            ("CENTER", "CENTER"),
                            ("HYPER", "HYPER"),
                            ("EXCLUSIVE", "EXCLUSIVE"),
                        ],
                        help_text="基本约束",
                        max_length=50,
                        verbose_name="基本约束",
                    ),
                ),
                (
                    "sort",
                    models.IntegerField(default=0, help_text="排序", verbose_name="排序"),
                ),
                (
                    "build",
                    models.ForeignKey(
                        help_text="构筑",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="spellcards",
                        to="game.build",
                        verbose_name="构筑",
                    ),
                ),
                (
                    "traits",
                    models.ManyToManyField(
                        help_text="特性",
                        related_name="spellcards",
                        to="game.trait",
                        verbose_name="特性",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        help_text="类型",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="game.type",
                        verbose_name="类型",
                    ),
                ),
            ],
            options={
                "verbose_name": "符卡",
                "verbose_name_plural": "符卡",
            },
        ),
        migrations.CreateModel(
            name="ExtendedConstraint",
            fields=[
                (
                    "id",
                    models.AutoField(
                        help_text="ID",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(help_text="类型", max_length=50, verbose_name="类型"),
                ),
                (
                    "effect",
                    models.CharField(help_text="效果", max_length=50, verbose_name="效果"),
                ),
                (
                    "sort",
                    models.IntegerField(default=0, help_text="排序", verbose_name="排序"),
                ),
                (
                    "spellcard",
                    models.ForeignKey(
                        help_text="符卡",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="extended_constraints",
                        to="game.spellcard",
                        verbose_name="符卡",
                    ),
                ),
            ],
            options={
                "verbose_name": "符卡扩展限制",
                "verbose_name_plural": "符卡扩展限制",
            },
        ),
        migrations.CreateModel(
            name="CharacterVersion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        help_text="ID",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "version",
                    models.CharField(
                        default="经典", help_text="版本", max_length=50, verbose_name="版本"
                    ),
                ),
                (
                    "rarity",
                    models.CharField(
                        choices=[
                            ("UC", "UC"),
                            ("C", "C"),
                            ("R", "R"),
                            ("SR", "SR"),
                            ("SSR", "SSR"),
                            ("ST", "ST"),
                            ("S", "S"),
                        ],
                        help_text="稀有度",
                        max_length=50,
                        verbose_name="稀有度",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="立绘", upload_to="card", verbose_name="立绘"
                    ),
                ),
                (
                    "line",
                    models.CharField(help_text="牌语", max_length=200, verbose_name="牌语"),
                ),
                (
                    "sort",
                    models.IntegerField(default=0, help_text="排序", verbose_name="排序"),
                ),
                (
                    "character",
                    models.ForeignKey(
                        help_text="角色",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="versions",
                        to="game.character",
                        verbose_name="角色",
                    ),
                ),
                (
                    "episode",
                    models.ForeignKey(
                        blank=True,
                        help_text="卡包",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="characters",
                        to="game.episode",
                        verbose_name="卡包",
                    ),
                ),
                (
                    "illustrator",
                    models.ForeignKey(
                        help_text="画师",
                        on_delete=django.db.models.deletion.PROTECT,
                        to="game.illustrator",
                        verbose_name="画师",
                    ),
                ),
            ],
            options={
                "verbose_name": "角色版本",
                "verbose_name_plural": "角色版本",
            },
        ),
        migrations.CreateModel(
            name="CharacterSkill",
            fields=[
                (
                    "id",
                    models.AutoField(
                        help_text="ID",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("SUPPORT", "SUPPORT"),
                            ("CENTER", "CENTER"),
                            ("HYPER", "HYPER"),
                        ],
                        help_text="类型",
                        max_length=50,
                        verbose_name="类型",
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="名字", max_length=50, verbose_name="名字"),
                ),
                ("description", models.TextField(help_text="描述", verbose_name="描述")),
                (
                    "sort",
                    models.IntegerField(default=0, help_text="排序", verbose_name="排序"),
                ),
                (
                    "character",
                    models.ForeignKey(
                        help_text="角色",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="skills",
                        to="game.character",
                        verbose_name="角色",
                    ),
                ),
            ],
            options={
                "verbose_name": "角色技能",
                "verbose_name_plural": "角色技能",
            },
        ),
        migrations.CreateModel(
            name="Version",
            fields=[
                (
                    "id",
                    models.AutoField(
                        help_text="ID",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "version",
                    models.CharField(
                        default="经典", help_text="版本", max_length=50, verbose_name="版本"
                    ),
                ),
                (
                    "rarity",
                    models.CharField(
                        choices=[
                            ("UC", "UC"),
                            ("C", "C"),
                            ("R", "R"),
                            ("SR", "SR"),
                            ("SSR", "SSR"),
                            ("ST", "ST"),
                            ("S", "S"),
                        ],
                        help_text="稀有度",
                        max_length=50,
                        verbose_name="稀有度",
                    ),
                ),
                (
                    "line",
                    models.CharField(help_text="牌语", max_length=200, verbose_name="牌语"),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="立绘", upload_to="card", verbose_name="立绘"
                    ),
                ),
                (
                    "sort",
                    models.IntegerField(default=0, help_text="排序", verbose_name="排序"),
                ),
                (
                    "episode",
                    models.ForeignKey(
                        blank=True,
                        help_text="卡包",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="game.episode",
                        verbose_name="卡包",
                    ),
                ),
                (
                    "illustrator",
                    models.ForeignKey(
                        help_text="画师",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="spellcards",
                        to="game.illustrator",
                        verbose_name="画师",
                    ),
                ),
                (
                    "spellcard",
                    models.ForeignKey(
                        help_text="符卡",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="versions",
                        to="game.spellcard",
                        verbose_name="符卡",
                    ),
                ),
            ],
            options={
                "verbose_name": "符卡版本",
                "verbose_name_plural": "符卡版本",
                "unique_together": {("spellcard", "version")},
            },
        ),
    ]
