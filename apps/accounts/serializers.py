from rest_framework import serializers
from apps.accounts.models import Employee, CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','email','password']
        extra_kwargs = {'password': {'write_only' : True}}
            
    def create(self, validate_data):
        return CustomUser.objects.create_user(**validate_data)
        

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields = '__all__'
