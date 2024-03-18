from google.auth.transport import requests
from google.oauth2 import id_token
from user.models import User
from django.contrib.auth import authenticate
from eccomerce.settings import base
from rest_framework.exceptions import AuthenticationFailed
import email


class Google():
    @staticmethod
    def validate(access_token):
        
        try:
            id_info = id_token.verify_oauth2_token(
                access_token, 
                requests.Request(), 
                base.GOOGLE_CLIENT_ID
            )
            if "accounts.google.com" in id_info["iss"]:
                return id_info
        except:
            return "Token is invalid or expired!"
        
def login_social_user(email,password):
    user=authenticate(email=email,password=password)
    user_token=user.tokens()
    return {
                "email":user.email,
                "full_name":user.get_full_name,
                "access_token":str(user_token.get("access")),
                "refresh_token":str(user_token.get("refresh"))
            }
    
def register_social_user(provider,email,first_name,last_name):
    user=User.objects.get(email=email)
    if user.exist():
        if provider== user.auth_provider:
            login_social_user(email,base.SOCIAL_AUTH_PASSWORD)
        else:
            raise AuthenticationFailed(
                detail=f"Please continue your login using {user.auth_provider}",
            )
    else:
        new_user={
            "email":email,
            "first_name":first_name,
            "last_name":last_name,
            "password":base.SOCIAL_AUTH_PASSWORD,
        }
        register_user=User.objects.create_user(**new_user)
        register_user.auth_provider=provider
        register_user.is_verified=True
        register_user.save()
        login_social_user(email,base.SOCIAL_AUTH_PASSWORD)
