from rest_framework.generics import GenericAPIView
from .serializer import GoogleInSerializer
from rest_framework.response import Response
from rest_framework import status


class GoogleSignInView(GenericAPIView):
    serializer_class = GoogleInSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=((serializer.validated_data)['access_token'])
        return Response(data, status=status.HTTP_200_OK) 
    
google_login_view=GoogleSignInView.as_view()