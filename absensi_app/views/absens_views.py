from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from ..serializers import AbsenSerializer
from ..models import Absen, Employee
from ..response_helper import ResponseHelper


class AbsenListView(APIView):
    
    def get(self, request, *args, **kwargs):
        absen_list = Absen.objects.all()
        serializer = AbsenSerializer(absen_list, many = True)
        print(f"serializer: {serializer.data}")
        return Response(serializer.data, status=status.HTTP_200_OK)

    # check in
    def post(self,request, *args, **kwargs):
        
        state = Absen.objects.filter(
                employee_uuid = request.data['employee_uuid'],
                date = datetime.now().date()).first()
        
        serializer = AbsenSerializer(data = request.data)
       
        if serializer.is_valid():  
            if not state :
                serializer.save()
                return ResponseHelper.success(
                    serializer.data,message = "check-in successfully",
                    status_code = status.HTTP_201_CREATED
                )
                
            return ResponseHelper.failed(
                message = "checkin already absent today",
                status_code = status.HTTP_200_OK
            )                
               
        return ResponseHelper.failed(
            message = serializer.errors,
        )
    
    # checkout
    def patch(self, request, *args, **kwargs):
        
        employee_uuid = request.data.get("employee_uuid")
        latitude = request.data.get("latitude")
        longitude = request.data.get("longitude")
        
        if not employee_uuid or not latitude or not longitude:
            return ResponseHelper.failed(
                message = 'employee_uuid, longitude and latitude field required'
            )
                        
        state = Absen.objects.filter(
                    employee_uuid = request.data['employee_uuid'],
                    date = datetime.now().date()
                ).first()
        
        serializer = AbsenSerializer(state, data = request.data, partial = True)
        
        
        if state is None:
            return ResponseHelper.failed(message="check-in first")
        
        
        if serializer.is_valid():
            if state.check_out != None:
                return ResponseHelper.failed(
                    message = "checkout already today !",
                    status_code = status.HTTP_200_OK
                )
            
            serializer.save(
                check_out = datetime.now(),
                longitude = longitude,
                latitude = latitude,
                status = "HADIR"
            )
            
            return ResponseHelper.success(
                message = 'checkout successfully',
                data = serializer.data,
                status_code = status.HTTP_202_ACCEPTED
            )

        
        return ResponseHelper.failed(message=serializer.errors)
        