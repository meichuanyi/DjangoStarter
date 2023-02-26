from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework import permissions

from .models import *
from .serializers import *


@method_decorator(name='list', decorator=swagger_auto_schema(operation_summary='获取所有作者资料'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='获取指定作者资料'))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='添加作者资料'))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_summary='修改指定作者资料'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='部分修改指定作者资料'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='删除指定作者资料'))
class AuthorViewSet(viewsets.ModelViewSet):
    """作者相关操作"""
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@method_decorator(name='list', decorator=swagger_auto_schema(operation_summary='获取所有文章资料'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='获取指定文章资料'))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='添加文章资料'))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_summary='修改指定文章资料'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='部分修改指定文章资料'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='删除指定文章资料'))
class ArticleViewSet(viewsets.ModelViewSet):
    """文章相关操作"""
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

