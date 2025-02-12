from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views as authtoken_view

# drf_yasg文档工具
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# DjangoStarter 配置
from config.django_starter import project_info
# DjangoStarter 主页
from django_starter.contrib.guide import views

urlpatterns = [
    path('', views.index),
    path('guide/', include('apps.demo.urls')),

    # DjangoStarter
    path('django-starter/', include('django_starter.urls')),

    # 管理后台
    path('admin/', include('django_starter.contrib.admin.urls')),  # 实现 admin 登录验证码
    path('admin/', admin.site.urls),

    # 验证码
    path('captcha/', include('captcha.urls')),

    # API认证
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', authtoken_view.obtain_auth_token),

    # 自定义
    path('oda/', include('apps.oda.urls')),
]

# 接口文档 仅调试模式可用
if settings.DEBUG:
    openapi_obj = openapi.Info(
        title=project_info.name,
        default_version='v1',
        description=project_info.description,
        terms_of_service="https://github.com/Deali-Axy/DjangoStarter",
        contact=openapi.Contact(email="feedback@deali.cn"),
        license=openapi.License(name="BSD License"),
    )
    schema_view = get_schema_view(
        openapi_obj,
        public=True,
        permission_classes=[permissions.AllowAny],
        # permission_classes=[permissions.IsAdminUser],
    )
    urlpatterns.extend([
        # AutoScheme接口文档
        path(f'api-docs/auto/', include_docs_urls(title=openapi_obj.title)),
        # Swagger文档
        path(f'api-docs/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
        path(f'api-docs/swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        # redoc文档
        path(f'api-docs/redoc/', schema_view.with_ui('redoc', cache_timeout=0))
    ])
