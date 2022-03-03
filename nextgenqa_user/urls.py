from django.urls import path, include
from .api import UserRegisterApi

urlpatterns = [
    path('api/v1/user_register', UserRegisterApi.as_view()),
]