from django.db import models
from apps.accounts.models import Employee

class Absen(models.Model):
    
    STATUS_CHOICE = [
        ('HADIR','hadir'),
        ('IZIN','izin'),
        ('SAKIT','sakit'),
        ('ALPHA','alpha'),
    ]
    
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
        return f"{self.employee_uuid.user.username} - {self.date}"
    
