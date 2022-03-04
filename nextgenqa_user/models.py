from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class NextGenQa_User(models.Model):
    user_id = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    username = models.CharField(max_length=30, unique=True)
    user_first_name = models.CharField(max_length=40)
    user_last_name = models.CharField(max_length=40)
    user_email = models.EmailField(unique=True)
    user_phone = models.IntegerField(unique=True)
    user_password = models.CharField(max_length=40)

    def __str__(self):
        return self.username
