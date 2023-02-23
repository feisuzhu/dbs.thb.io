# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
from django.db import models
from martor import models as martor_models

# -- own --

# -- code --
_ = lambda s: {'help_text': s, 'verbose_name': s}


class Article(models.Model):
    id         = models.AutoField(primary_key=True)
    slug       = models.SlugField(**_("Slug"), unique=True)
    category   = models.CharField(**_("分类"), max_length=100)
    title      = models.CharField(max_length=255, **_('标题'))
    content    = martor_models.MartorField(**_('内容'))
    created_at = models.DateTimeField(auto_now_add=True, **_('创建时间'))
    updated_at = models.DateTimeField(auto_now=True, **_('更新时间'))

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title


class InfoBlockCategory(models.TextChoices):
    SOCIAL_GROUP = 'SOCIAL_GROUP', "社群"
    SHOP         = 'SHOP', "商店"
    BUILD_SHARE  = 'BUILD_SHARE', "构筑分享"



class InfoBlock(models.Model):
    id          = models.AutoField(primary_key=True)
    category    = models.CharField(max_length=50, **_("分类"), choices=InfoBlockCategory.choices)
    type        = models.CharField(**_("类型"), max_length=100)
    title       = models.CharField(max_length=255, **_('标题'))
    subtitle    = models.CharField(max_length=255, **_('副标题'))
    description = models.CharField(max_length=255, **_('描述'))
    image       = models.ImageField(**_('图片'), upload_to='page')
    content     = models.TextField(**_('内容'))
    sort        = models.IntegerField(**_('排序'))

    class Meta:
        verbose_name = '信息卡片'
        verbose_name_plural = '信息卡片'

    def __str__(self):
        return self.title


class InfoBlockButton(models.Model):
    id    = models.AutoField(primary_key=True)
    block = models.ForeignKey(InfoBlock, on_delete=models.CASCADE, **_('信息卡片'), related_name='buttons')
    title = models.CharField(max_length=255, **_('标题'))
    icon  = models.CharField(max_length=255, **_('图标'))
    color = models.CharField(max_length=255, **_('颜色'))
    url   = models.CharField(max_length=255, **_('链接'))
    sort  = models.IntegerField(**_('排序'))

    class Meta:
        verbose_name = '信息卡片按钮'
        verbose_name_plural = '信息卡片按钮'

    def __str__(self):
        return self.title


class Landing(models.Model):
    logo = models.ImageField(**_('Logo'), upload_to='page')
    monologo = models.ImageField(**_('单色 Logo'), upload_to='page')
    small_slogan = models.CharField(max_length=255, **_('小号字 Slogan'))
    big_slogan = models.CharField(max_length=255, **_('大号字 Slogan'))
    footer = models.TextField(**_('页脚'))

    class Meta:
        verbose_name = '首页'
        verbose_name_plural = '首页'

    def __str__(self):
        return '首页（只能有一个）'


class LandingWork(models.Model):
    id          = models.AutoField(primary_key=True)
    landing     = models.ForeignKey(Landing, on_delete=models.CASCADE, **_('首页'), related_name='works')
    image       = models.ImageField(**_('图片'), upload_to='page')
    title       = models.CharField(max_length=255, **_('标题'))
    subtitle    = models.CharField(max_length=255, **_('副标题'))
    description = models.CharField(max_length=255, **_('描述'))
    url         = models.CharField(max_length=255, **_('链接'))
    urltext     = models.CharField(max_length=255, **_('链接文字'))
    sort        = models.IntegerField(**_('排序'))

    class Meta:
        verbose_name = '首页作品栏目'
        verbose_name_plural = '首页作品栏目'

    def __str__(self):
        return self.title


class LandingColumn(models.Model):
    id          = models.AutoField(primary_key=True)
    landing     = models.ForeignKey(Landing, on_delete=models.CASCADE, **_('首页'), related_name='columns')
    title       = models.CharField(max_length=255, **_('标题'))
    subtitle    = models.CharField(max_length=255, **_('副标题'))
    description = models.CharField(max_length=255, **_('描述'))
    url         = models.CharField(max_length=255, **_('链接'))
    urltext     = models.CharField(max_length=255, **_('链接文字'))
    sort        = models.IntegerField(**_('排序'))

    class Meta:
        verbose_name = '首页下方栏目'
        verbose_name_plural = '首页下方栏目'

    def __str__(self):
        return self.title


class LandingSlide(models.Model):
    id      = models.AutoField(primary_key=True)
    landing = models.ForeignKey(Landing, on_delete=models.CASCADE, **_('首页'), related_name='slides')
    image   = models.ImageField(**_('图片'), upload_to='page')
    url     = models.CharField(max_length=255, **_('链接'))
    sort    = models.IntegerField(**_('排序'))

    class Meta:
        verbose_name = '首页幻灯片'
        verbose_name_plural = '首页幻灯片'

    def __str__(self):
        return self.url


class OutboundLink(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, **_('名称'))
    icon = models.ImageField(**_('图标'), upload_to='page')
    mono = models.ImageField(**_('单色图标'), upload_to='page')
    url  = models.CharField(max_length=255, **_('链接'))
    sort = models.IntegerField(**_('排序'))

    class Meta:
        verbose_name = '外链'
        verbose_name_plural = '外链'


class Page(models.Model):
    id      = models.AutoField(primary_key=True)
    slug    = models.SlugField(**_('Slug'), unique=True)
    content = martor_models.MartorField(**_('内容'))

    class Meta:
        verbose_name = '单页'
        verbose_name_plural = '单页'

    def __str__(self):
        return self.slug
