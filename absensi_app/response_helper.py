from rest_framework.views import Response,status

class ResponseHelper:
    
    @staticmethod
    def success(data = None, message = "success",status_code = status.HTTP_200_OK):
        
        return Response({
            'status' : 'success',
            'message' : message,
            'data' : data,
        }, status=status_code)
        
    @staticmethod
    def failed(message = "error", status_code = status.HTTP_400_BAD_REQUEST):
        return Response({
            'status' :'error',
            'message' : message,
            'data' : None
        },status=status_code)
        