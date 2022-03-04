from rest_framework import  serializers
from .models import NextGenQa_User
from django.contrib.auth.models import User



class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextGenQa_User
        fields = ('username', 'user_first_name', 'user_last_name', 'user_email','user_phone','user_password')
        extra_kwargs = {
            'user_password': {'write_only': True},
        }

    def create(self, validated_data):
        user = NextGenQa_User.objects.create(**validated_data)
        # user = NextGenQa_User.objects.create(validated_data['username'], user_password=validated_data['user_password'],
        #                                 user_first_name=validated_data['user_first_name'], user_last_name=validated_data['user_last_name'],
        #                                           user_email=validated_data['user_email'],user_phone=validated_data['user_phone'])
        return user


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextGenQa_User
        fields = '__all__'