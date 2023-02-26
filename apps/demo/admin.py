from django.contrib import admin

from .models import *


@admin.register(DemoDepartment)
class DemoDepartmentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'id', 'is_deleted', 'created_time', 'updated_time', 'name', ]

