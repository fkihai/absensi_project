import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    
    ROLE_CHOICES = (
        ('employee', 'Employee'),
        ('hr', 'HR'),        ('manager', 'Manager'),
        ('admin', 'Admin'),
    )
    
    email  = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')   

    # email-based login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return f"{self.username} : {self.role}"


class Employee(models.Model):
    
    id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="employee_profile", null=False, blank=False)
    nip = models.CharField(max_length=20, unique=True)
    departement = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}"

