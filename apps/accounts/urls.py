
from django.urls import path, include
from apps.accounts.views import EmployeeViewSet 
from rest_framework.routers import DefaultRouter

# generate url api crud
router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls)),
]