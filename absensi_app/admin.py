from django.contrib import admin
from .models import Employee, Absen


# Register your models here.

class AbsensiAdmin(admin.ModelAdmin):
    readonly_fields = ['check_in', 'check_out']


admin.site.register(Employee)
admin.site.register(Absen, AbsensiAdmin)

