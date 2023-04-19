# Generated by Django 4.1.7 on 2023-04-20 15:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import martor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ArticleCategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "slug",
                    models.SlugField(
                        help_text="Slug", unique=True, verbose_name="Slug"
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="名称", max_length=100, verbose_name="名称"),
                ),
                ("sort", models.IntegerField(help_text="排序", verbose_name="排序")),
                ("hidden", models.BooleanField(help_text="隐藏", verbose_name="隐藏")),
            ],
            options={
                "verbose_name": "文章分类",
                "verbose_name_plural": "文章分类",
                "ordering": ("sort", "id"),
            },
        ),
        migrations.CreateModel(
            name="InfoBlock",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("COMMUNITY", "社群"),
                            ("SHOP", "商店"),
                            ("DECK_SHARE", "卡组分享"),
                        ],
                        help_text="分类",
                        max_length=50,
                        verbose_name="分类",
                    ),
                ),
                (
                    "type",
                    models.CharField(help_text="类型", max_length=100, verbose_name="类型"),
                ),
                (
                    "title",
                    models.CharField(help_text="标题", max_length=255, verbose_name="标题"),
                ),
                (
                    "subtitle",
                    models.CharField(
                        help_text="副标题", max_length=255, verbose_name="副标题"
                    ),
                ),
                (
                    "description",
                    models.CharField(help_text="描述", max_length=255, verbose_name="描述"),
                ),
                (
                    "image",
                    models.ImageField(
                        help_text="图片", upload_to="page", verbose_name="图片"
                    ),
                ),
                ("sort", models.IntegerField(help_text="排序", verbose_name="排序")),
            ],
            options={
                "verbose_name": "信息卡片",
                "verbose_name_plural": "信息卡片",
                "ordering": ("sort", "id"),
            },
        ),
        migrations.CreateModel(
            name="Landing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        help_text="Logo（554x130）", upload_to="page", verbose_name="Logo"
                    ),
                ),
                (
                    "monologo",
                    models.ImageField(
                        help_text="单色 Logo（554x130）",
                        upload_to="page",
                        verbose_name="单色 Logo",
                    ),
                ),
                (
                    "small_slogan",
                    models.CharField(
                        help_text="小号字 Slogan",
                        max_length=255,
                        verbose_name="小号字 Slogan",
                    ),
                ),
                (
                    "big_slogan",
                    models.CharField(
                        help_text="大号字 Slogan",
                        max_length=255,
                        verbose_name="大号字 Slogan",
                    ),
                ),
                ("footer", models.TextField(help_text="页脚", verbose_name="页脚")),
            ],
            options={
                "verbose_name": "首页",
                "verbose_name_plural": "首页",
            },
        ),
        migrations.CreateModel(
            name="OutboundLink",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "name",
                    models.CharField(help_text="名称", max_length=255, verbose_name="名称"),
                ),
                (
                    "icon",
                    models.ImageField(
                        help_text="图标", upload_to="page", verbose_name="图标"
                    ),
                ),
                (
                    "mono",
                    models.ImageField(
                        help_text="单色图标", upload_to="page", verbose_name="单色图标"
                    ),
                ),
                (
                    "url",
                    models.CharField(help_text="链接", max_length=255, verbose_name="链接"),
                ),
                ("sort", models.IntegerField(help_text="排序", verbose_name="排序")),
            ],
            options={
                "verbose_name": "外链",
                "verbose_name_plural": "外链",
                "ordering": ("sort", "id"),
            },
        ),
        migrations.CreateModel(
            name="LandingWork",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "image",
                    models.ImageField(
                        help_text="图片（640x448）", upload_to="page", verbose_name="图片"
                    ),
                ),
                (
                    "title",
                    models.CharField(help_text="标题", max_length=255, verbose_name="标题"),
                ),
                (
                    "subtitle",
                    models.CharField(
                        help_text="副标题", max_length=255, verbose_name="副标题"
                    ),
                ),
                (
                    "description",
                    models.CharField(help_text="描述", max_length=255, verbose_name="描述"),
                ),
                (
                    "url",
                    models.CharField(help_text="链接", max_length=255, verbose_name="链接"),
                ),
                (
                    "urltext",
                    models.CharField(
                        help_text="链接文字", max_length=255, verbose_name="链接文字"
                    ),
                ),
                ("sort", models.IntegerField(help_text="排序", verbose_name="排序")),
                (
                    "landing",
                    models.ForeignKey(
                        help_text="首页",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="works",
                        to="page.landing",
                        verbose_name="首页",
                    ),
                ),
            ],
            options={
                "verbose_name": "首页作品栏目",
                "verbose_name_plural": "首页作品栏目",
                "ordering": ("sort", "id"),
            },
        ),
        migrations.CreateModel(
            name="LandingSlide",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "image",
                    models.ImageField(
                        help_text="图片（1920x690）", upload_to="page", verbose_name="图片"
                    ),
                ),
                (
                    "url",
                    models.CharField(help_text="链接", max_length=255, verbose_name="链接"),
                ),
                ("sort", models.IntegerField(help_text="排序", verbose_name="排序")),
                (
                    "landing",
                    models.ForeignKey(
                        help_text="首页",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="slides",
                        to="page.landing",
                        verbose_name="首页",
                    ),
                ),
            ],
            options={
                "verbose_name": "首页幻灯片",
                "verbose_name_plural": "首页幻灯片",
                "ordering": ("sort", "id"),
            },
        ),
        migrations.CreateModel(
            name="LandingColumn",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(help_text="标题", max_length=255, verbose_name="标题"),
                ),
                (
                    "subtitle",
                    models.CharField(
                        help_text="副标题", max_length=255, verbose_name="副标题"
                    ),
                ),
                (
                    "description",
                    models.CharField(help_text="描述", max_length=255, verbose_name="描述"),
                ),
                (
                    "url",
                    models.CharField(help_text="链接", max_length=255, verbose_name="链接"),
                ),
                (
                    "urltext",
                    models.CharField(
                        help_text="链接文字", max_length=255, verbose_name="链接文字"
                    ),
                ),
                ("sort", models.IntegerField(help_text="排序", verbose_name="排序")),
                (
                    "landing",
                    models.ForeignKey(
                        help_text="首页",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="columns",
                        to="page.landing",
                        verbose_name="首页",
                    ),
                ),
            ],
            options={
                "verbose_name": "首页下方栏目",
                "verbose_name_plural": "首页下方栏目",
                "ordering": ("sort", "id"),
            },
        ),
        migrations.CreateModel(
            name="InfoBlockButton",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "title",
                    models.CharField(help_text="标题", max_length=255, verbose_name="标题"),
                ),
                (
                    "color",
                    models.CharField(help_text="颜色", max_length=255, verbose_name="颜色"),
                ),
                (
                    "url",
                    models.CharField(help_text="链接", max_length=255, verbose_name="链接"),
                ),
                ("sort", models.IntegerField(help_text="排序", verbose_name="排序")),
                (
                    "block",
                    models.ForeignKey(
                        help_text="信息卡片",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="buttons",
                        to="page.infoblock",
                        verbose_name="信息卡片",
                    ),
                ),
            ],
            options={
                "verbose_name": "信息卡片按钮",
                "verbose_name_plural": "信息卡片按钮",
                "ordering": ("sort", "id"),
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "slug",
                    models.SlugField(
                        help_text="Slug", unique=True, verbose_name="Slug"
                    ),
                ),
                (
                    "title",
                    models.CharField(help_text="标题", max_length=255, verbose_name="标题"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="图片（1398x612）",
                        null=True,
                        upload_to="page",
                        verbose_name="图片",
                    ),
                ),
                (
                    "content",
                    martor.models.MartorField(help_text="内容", verbose_name="内容"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text="创建时间",
                        verbose_name="创建时间",
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="更新时间", verbose_name="更新时间"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        help_text="分类",
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="articles",
                        to="page.articlecategory",
                        verbose_name="分类",
                    ),
                ),
            ],
            options={
                "verbose_name": "文章",
                "verbose_name_plural": "文章",
            },
        ),
    ]
