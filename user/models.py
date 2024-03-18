from django.db import models
from django.utils import timezone
from .managers import UserManager
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken


AUTH_PROVIDERS = {
    "email":"Email",
    "google":"Google",
    "facebook":"Facebook",
    "twitter":"Twitter",
    "github":"Github",
}


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","last_name"]
    email = models.CharField(
        max_length=100, 
        unique=True,
        null=False,
        blank=False
    )
    first_name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    last_name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    avatar = models.ImageField(
        default="avatar.png",
        upload_to="media/avatar/"
    )
    date_joined = models.DateTimeField(
        default=timezone.now
    )
    is_staff = models.BooleanField(
        default=False
    )
    is_superuser = models.BooleanField(
        default=False
    )
    is_verified = models.BooleanField(
        default=False
    )
    last_login = models.DateTimeField(
        auto_now=True
    )
    objects = UserManager(
        
    )
    auth_provider=models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default=AUTH_PROVIDERS.get('email')
    )
    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def tokens(self):
        refresh=RefreshToken.for_user(self)
        return {
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
    
    class Meta:
        ordering = ["-date_joined"]
        
        
class OneTimePassword(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    code = models.CharField(
        max_length=10, 
        unique=True
    )
    def __str__(self):
        return f"{self.user}--passcode"
    
