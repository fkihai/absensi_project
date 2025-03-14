from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class Employee(models.Model):
    
    # id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    nip = models.CharField(max_length=20, blank=False, unique=True)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False, unique=True)
    position = models.CharField(max_length=50, blank=True)
    departement = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=13, blank=True)
    address = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Employee : {self.name}"


class Absen(models.Model):
    
    STATUS_CHOICE = [
        ('HADIR','hadir'),
        ('IZIN','izin'),
        ('SAKIT','sakit'),
        ('ALPHA','alpha'),
    ]
    
    # id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_uuid = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='absensi')
    date = models.DateField(auto_now_add=True)
    check_in = models.DateTimeField(auto_now_add=True,null=False, blank=False)
    check_out = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='ALPHA')
    latitude = models.FloatField(blank=False, null=False)
    longitude = models.FloatField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.employee_uuid.name} - {self.date}"
    
