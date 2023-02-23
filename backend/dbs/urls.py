# -*- coding: utf-8 -*-

"""dbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# -*- coding: utf-8 -*-

# -- stdlib --
# -- third party --
from django.apps import apps
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path as url
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

# -- own --
from .graphql import schema
from page.views import markdown_uploader


# -- code --
admin.site.site_header = '幻想梦斗符公式站'
apps.get_app_config('auth').sort_order = 10

urlpatterns = [
    path('graphql', csrf_exempt(GraphQLView.as_view(schema=schema, graphiql=True))),
    path("admin/", admin.site.urls),
    url(
        r'^martor/uploader/$',
        markdown_uploader, name='markdown_uploader_page'
    ),
    path('martor/', include('martor.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
