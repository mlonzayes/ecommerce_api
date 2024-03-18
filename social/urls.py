from django.urls import path
from . import views


urlpatterns = [
    path("google/",views.google_login_view,name="google")
]
