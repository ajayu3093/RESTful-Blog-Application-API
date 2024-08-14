from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LoginSerializer, RegisterSerializer
from rest_framework import status


class RegisterView(APIView):
    def post(self, request):
        
        try:
            data = request.data
            serializer = RegisterSerializer(data=data)
            
            if not serializer.is_valid():
                return Response(
                    {
                        'data': serializer.errors,
                        'message': 'Something went wrong'
                    }, status=status.HTTP_400_BAD_REQUEST
                )
                
            serializer.save()
            
            return Response(
                {
                    'data': {},
                    'message': 'User registered successfully'
                }, status=status.HTTP_201_CREATED
            )
                
        except Exception as e:
            print(e)
            return Response(
                {
                    'data': {},
                    'message': str(e)
                }, status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data=data)
            
            if not serializer.is_valid():
                return Response(
                    {
                        'data': serializer.errors,
                        'message': 'Something went wrong'
                    }, status=status.HTTP_400_BAD_REQUEST
                )
                
            response = serializer.get_jwt_token(serializer.data)
            
            return Response(response, status=status.HTTP_200_OK)
        
        except Exception as e:
            print(e)
            return Response(
                {
                    'data': {},
                    'message': str(e)
                }, status=status.HTTP_400_BAD_REQUEST
            )