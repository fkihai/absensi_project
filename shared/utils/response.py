from rest_framework.response import Response
from rest_framework import status

class ResponseHelper:
    
    @staticmethod
    def success(data = None, message = "success",status_code = status.HTTP_200_OK):
        
        return Response({
            'status' : 'success',
            'message' : message,
            'data' : data,
        }, status=status_code)
        
    @staticmethod
    def failed(data = None, message = "failed", status_code = status.HTTP_400_BAD_REQUEST):
        return Response({
            'status' :'failed',
            'message' : message,
            'data' : data
        },status=status_code)
        