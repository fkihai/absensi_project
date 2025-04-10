from rest_framework import serializers
from apps.accounts.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields = '__all__'
