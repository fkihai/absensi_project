from rest_framework import serializers
from apps.absensi.models import Absen


class AbsenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Absen
        fields = '__all__'
        read_only_fields = ['date','check_in','check_out','created_at','updated_at']