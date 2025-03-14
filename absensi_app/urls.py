
from django.urls import path, include
from .views.absens_views import AbsenListView 
from .views.employee_views import EmployeeViewSet 
from rest_framework.routers import DefaultRouter

# generate url api crud
router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
    path('absen/', AbsenListView.as_view())
]