#from django.conf.urls import url
from django.urls import path, include
from .api import ContribRegisterApi

urlpatterns = [
    path('api/v1/contrib_register', ContribRegisterApi.as_view()),
]