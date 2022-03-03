from rest_framework import  serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from .models import NextGenQa_Contributor
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class ContribRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextGenQa_Contributor
        fields = ('id', 'contrib_username', 'contrib_user_first_name', 'contrib_user_last_name', 'contrib_user_email','contrib_user_phone','contrib_user_password')
        extra_kwargs = {
            'contrib_user_password': {'write_only': True},
        }

    def create(self, validated_data):
        user = NextGenQa_Contributor.objects.create_user(validated_data['username'], contrib_user_password=validated_data['contrib_user_password'],
                                        contrib_user_first_name=validated_data['contrib_user_first_name'], contrib_user_last_name=validated_data['contrib_user_last_name'],
                                                         contrib_user_email=validated_data['contrib_user_email'],contrib_user_phone=validated_data['contrib_user_phone'])
        return user


# User serializer
class ContribSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextGenQa_Contributor
        fields = '__all__'