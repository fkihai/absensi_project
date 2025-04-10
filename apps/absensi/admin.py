from django.contrib import admin
from apps.absensi.models import Absen


# Register your models here.

class AbsensiAdmin(admin.ModelAdmin):
    readonly_fields = ['check_in', 'check_out']


admin.site.register(Absen,AbsensiAdmin)
