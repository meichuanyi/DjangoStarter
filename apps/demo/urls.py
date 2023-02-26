from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import *

router = DefaultRouter()

router.register('demo_department', DemoDepartmentViewSet, basename='demo_department')



urlpatterns = [
    path('', include(router.urls))
]