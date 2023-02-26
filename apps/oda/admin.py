from django.contrib import admin

from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'name', ]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'name', 'content', 'author', ]

