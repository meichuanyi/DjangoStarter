from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .viewsets import *

router = DefaultRouter()

router.register('author', AuthorViewSet, basename='author')

router.register('article', ArticleViewSet, basename='article')



urlpatterns = [
    path('', include(router.urls)),
    path('admin_home', views.extend_admin_home),
    path('test', views.test)
]