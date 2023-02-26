from rest_framework import serializers
from .models import *


class DemoDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemoDepartment
        fields = '__all__'

