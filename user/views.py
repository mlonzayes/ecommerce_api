from . import serializer
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import OneTimePassword
from .utils import send_code_to_user
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str,DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import User
from rest_framework.views import APIView


class UserRegister(generics.CreateAPIView):
    serializer_class = serializer.RegisterUserSerializer
    
    def post(self, request, *args, **kwargs):
        try:
            user_data=request.data
            serializer = self.serializer_class(data=user_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                user=serializer.data
                send_code_to_user(user['email'])
                return Response(
                    {
                    "data":user,
                    "message":f"hi {user['first_name']} thanks for signing up! a passcode has be sent to your email. Please complete verification!",
                    "status":status.HTTP_200_OK
                    }, 
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)    
    
          
user_register=UserRegister.as_view()


class VerifyUserEmail(APIView):
    
    def post(self,request):
        otpcode=request.data.get('otp')
        try:
            user_code_obj=OneTimePassword.objects.get(code=otpcode)
            user=user_code_obj.user
            if not user.is_verified:
                user.is_verified=True
                user.save()
                return Response(
                    {
                    "message":"user verified successfully",
                    "status":status.HTTP_200_OK
                    },
                    status=status.HTTP_200_OK
                )
            return Response(
                {
                    "message":"user already verified",
                    "status":status.HTTP_500_INTERNAL_SERVER_ERROR
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except OneTimePassword.DoesNotExist:
            return Response({"error": "passcode not provided"}, status=status.HTTP_400_BAD_REQUEST)
      
      
user_verify=VerifyUserEmail.as_view()
  
class LoginUserView(generics.GenericAPIView):
    serializer_class=serializer.LoginUserSerializer
    
    def post(self,request):
        serializer=self.serializer_class(data=self.request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(
            {
            "data":serializer.data,
            "message":"Login succesfully!"
            },
            status=status.HTTP_200_OK
        )

user_login=LoginUserView.as_view()


class PasswordResetRequestView(generics.GenericAPIView):
    serializer_class=serializer.PasswordResetSerializer

    def post(self, request):
        serializer=self.serializer_class(data=self.request.data,context={'request':request})
        
        serializer.is_valid(raise_exception=True)
        return Response({
            "message":"a link has been sent to your email to reset your password"
        },
        status=status.HTTP_200_OK
        )

user_password_reset_request=PasswordResetRequestView.as_view()
        
class PasswordResetConfirmView(generics.GenericAPIView):
    def get(self, request,uidb64,token):
        try:
            user_id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response(
                    {
                    "error":"invalid token"
                    }, 
                    status=status.HTTP_401_UNAUTHORIZED
            )
            return Response(
                {
                    'status':status.HTTP_200_OK,
                    'message':'credential is valid',
                    'uidb64':uidb64,
                    'token':token
                },
                status=status.HTTP_200_OK
            )
        except DjangoUnicodeDecodeError:
            return Response({
                "status":status.HTTP_401_UNAUTHORIZED,
                "error":"token is invalid or has expired"
                }, 
                status=status.HTTP_401_UNAUTHORIZED
            )

user_password_reset_confirm=PasswordResetConfirmView.as_view()
       
class SetNewPasswordView(generics.GenericAPIView):
    serializer_class=serializer.SetNewPasswordSerializer

    def patch(self,request):
        serializer=self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "message":"password reset successfull",
            "status":status.HTTP_200_OK
            },
            status=status.HTTP_200_OK
            )

user_password_reset_patch=SetNewPasswordView.as_view()


class LogoutUserView(generics.GenericAPIView):
    serializer_class=serializer.LogoutUserSerializer
    permission_classes=[IsAuthenticated]

    def post(self, request):
        serializer=self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            status=status.HTTP_204_NO_CONTENT,
        )
user_logout=LogoutUserView.as_view()