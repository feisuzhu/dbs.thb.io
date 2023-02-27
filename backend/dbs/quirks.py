def quirk_add_admin_sorting():
    from django.contrib import admin
    from django.apps import apps

    def get_app_list(self, request, app_label=None):
        app_dict = self._build_app_dict(request, app_label)

        from django.contrib.admin.sites import site

        app_list = []

        for app_name in app_dict.keys():
            app = app_dict[app_name]
            model_priority = {
                model['object_name']: getattr(
                    site._registry[apps.get_model(app_name, model['object_name'])],
                    'sort_order',
                    10000
                ) for model in app['models']
            }
            app['models'].sort(key=lambda x: (model_priority[x['object_name']], x['name'].lower()))
            app_list.append(app)

        def app_order(a):
            return getattr(apps.get_app_config(a['app_label']), 'sort_order', 10000)

        app_list = sorted(app_list, key=lambda x: (app_order(x), x['name'].lower()))

        return app_list

    admin.AdminSite.get_app_list = get_app_list


def quirk_fix_autofield_graphql_type():
    from graphene_django.converter import convert_django_field, convert_field_to_int
    from django.db import models

    convert_django_field.register(models.AutoField)(convert_field_to_int)


def quirk_add_image_field_graphql_type():
    import graphene as gh
    from graphene_django.converter import convert_django_field
    from django.db import models

    class ImagePathType(gh.Enum):
        FULL = 1
        RAW  = 2

    def image_resolver(root, info, type=ImagePathType.FULL):
        f = getattr(root, info.field_name)
        if not f:
            return None

        if type == ImagePathType.FULL:
            return f.url
        elif type == ImagePathType.RAW:
            return f
        else:
            raise Exception('Invalid image type')

    def convert_field_to_image(field, registry=None):
        return gh.Field(gh.String,
            type=gh.Argument(ImagePathType, description='图片路径类型', required=True, default_value=ImagePathType.FULL),
            description=field.help_text and str(field.help_text),
            required=not field.null,
            resolver=image_resolver,
        )

    convert_django_field.register(models.ImageField)(convert_field_to_image)


def quirk_add_martor_field_graphql_type():
    import graphene as gh
    from graphene_django.converter import convert_django_field
    from django.utils.safestring import mark_safe
    from martor.models import MartorField
    from martor.utils import markdownify

    class MarkdownFieldType(gh.Enum):
        RAW  = 0
        RENDERED = 1
        EXCERPT = 2

    def martor_resolver(root, info, type=MarkdownFieldType.RENDERED):
        f = getattr(root, info.field_name)

        if type == MarkdownFieldType.RENDERED:
            return mark_safe(markdownify(f))
        elif type == MarkdownFieldType.EXCERPT:
            return f.encode('utf-8')[:500].decode('utf-8', 'ignore')
        elif type == MarkdownFieldType.RAW:
            return f
        else:
            raise Exception('Invalid markdown field type')

    def convert_field_to_martor(field, registry=None):
        return gh.Field(gh.String,
            type=gh.Argument(MarkdownFieldType, description='渲染参数', required=True, default_value=MarkdownFieldType.RENDERED),
            description=field.help_text and str(field.help_text),
            required=not field.null,
            resolver=martor_resolver,
        )

    convert_django_field.register(MartorField)(convert_field_to_martor)


def apply_quirks():
    for n, f in list(globals().items()):
        if n.startswith('quirk_'):
            f()
