from django.db import models

# Create your models here.
from django.db import models


class Author(models.Model):
    name = models.CharField('作者名称', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '作者'
        verbose_name_plural = verbose_name


class Article(models.Model):
    name = models.CharField('文章名称', max_length=20)
    content = models.TextField('文章内容')
    author = models.ForeignKey('Author', verbose_name='文章作者', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name