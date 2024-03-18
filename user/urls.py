from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.user_register,name='register'),
    path('verify-email/',views.user_verify,name='verify'),
    path('login/', views.user_login, name='login'),
    path('password-reset/', views.user_password_reset_request, name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/',views.user_password_reset_confirm, name='password-reset-confirm'),
    path('password-reset-complete/', views.user_password_reset_patch, name='password-reset-complete'),
    path('logout/', views.user_logout, name='logout'),
]
