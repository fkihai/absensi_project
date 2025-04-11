
from django.urls import path
from apps.absensi.views import AbsenListView 

urlpatterns = [
    path('absen/', AbsenListView.as_view(), name="absensi")
]