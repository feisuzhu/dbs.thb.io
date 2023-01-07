from django.apps import AppConfig


class PageConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "page"
    verbose_name = "页面"
    sort_order = 20
