from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework import permissions

from .models import *
from .serializers import *


@method_decorator(name='list', decorator=swagger_auto_schema(operation_summary='获取所有部门资料'))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(operation_summary='获取指定部门资料'))
@method_decorator(name='create', decorator=swagger_auto_schema(operation_summary='添加部门资料'))
@method_decorator(name='update', decorator=swagger_auto_schema(operation_summary='修改指定部门资料'))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(operation_summary='部分修改指定部门资料'))
@method_decorator(name='destroy', decorator=swagger_auto_schema(operation_summary='删除指定部门资料'))
class DemoDepartmentViewSet(viewsets.ModelViewSet):
    """部门相关操作"""
    serializer_class = DemoDepartmentSerializer
    queryset = DemoDepartment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

