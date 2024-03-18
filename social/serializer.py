from rest_framework import serializers
from . import utils
from eccomerce.settings import base
from rest_framework.exceptions import AuthenticationFailed



class GoogleInSerializer(serializers.Serializer):
    access_token = serializers.CharField(min_length=6, max_length=500)
    
    def validate_accesss_token(self, access_token):
        google_user_data=utils.Google.validate(access_token)
        try:
            user_id=google_user_data["sub"]
            
        except AuthenticationFailed:
            raise serializers.ValidationError("Invalid access token")
        
        if google_user_data['aud'] != base.GOOGLE_CLIENT_ID:
            raise serializers.ValidationError("Could not verify!")
        
        email=google_user_data["email"]
        first_name=google_user_data["given_name"]
        last_name=google_user_data["family_name"]
        provider="google"
        
        return utils.register_social_user(provider,email,first_name,last_name)