from rest_framework import viewsets,status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from apps.accounts.models import Employee
from apps.accounts.serializers import EmployeeSerializer, RegisterSerializer
from shared.utils.response import ResponseHelper

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return ResponseHelper.success(
            message=f"delete profile user {instance.user.username} successfully",
            status_code=status.HTTP_204_NO_CONTENT
        )
        
class RegisterView(APIView):

    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return ResponseHelper.success(
                    message = "user created successfully",
                    status_code = status.HTTP_201_CREATED,
                )
        except Exception as e:
            return ResponseHelper.failed(message=e)
            
        return ResponseHelper.failed(
            message = serializer.errors,
        )
