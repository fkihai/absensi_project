from django.shortcuts import render
from rest_framework import viewsets
from apps.accounts.models import Employee
from apps.accounts.serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
