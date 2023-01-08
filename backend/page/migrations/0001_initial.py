# Generated by Django 4.1.4 on 2023-01-08 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                    "category",
                    models.CharField(help_text="分类", max_length=100, verbose_name="分类"),
                ),
                (
                    "title",
                    models.CharField(help_text="标题", max_length=255, verbose_name="标题"),
                ),
                ("content", models.TextField(help_text="内容", verbose_name="内容")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="创建时间", verbose_name="创建时间"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, help_text="更新时间", verbose_name="更新时间"
                    ),
                ),
            ],
            options={
                "verbose_name": "文章",
                "verbose_name_plural": "文章",
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
                            ("SOCIAL_GROUP", "社群"),
                            ("SHOP", "商店"),
                            ("BUILD_SHARE", "构筑分享"),
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
                ("content", models.TextField(help_text="内容", verbose_name="内容")),
                ("sort", models.IntegerField(help_text="排序", verbose_name="排序")),
            ],
            options={
                "verbose_name": "信息卡片",
                "verbose_name_plural": "信息卡片",
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
                        help_text="Logo", upload_to="page", verbose_name="Logo"
                    ),
                ),
                (
                    "monologo",
                    models.ImageField(
                        help_text="单色 Logo", upload_to="page", verbose_name="单色 Logo"
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
            },
        ),
        migrations.CreateModel(
            name="Page",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "slug",
                    models.SlugField(
                        help_text="Slug", unique=True, verbose_name="Slug"
                    ),
                ),
                ("content", models.TextField(help_text="内容", verbose_name="内容")),
            ],
            options={
                "verbose_name": "单页",
                "verbose_name_plural": "单页",
            },
        ),
        migrations.CreateModel(
            name="LandingWork",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "image",
                    models.ImageField(
                        help_text="图片", upload_to="page", verbose_name="图片"
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
            },
        ),
        migrations.CreateModel(
            name="LandingSlide",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "image",
                    models.ImageField(
                        help_text="图片", upload_to="page", verbose_name="图片"
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
                    "icon",
                    models.CharField(help_text="图标", max_length=255, verbose_name="图标"),
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
            },
        ),
    ]
