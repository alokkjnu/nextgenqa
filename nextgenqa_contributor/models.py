from django.db import models


# Create your models here.
class NextGenQa_Contributor(models.Model):
    contrib_user_id = models.IntegerField(auto_created=True, unique=True, primary_key=True)
    contrib_username = models.CharField(max_length=30, unique=True)
    contrib_user_first_name = models.CharField(max_length=40)
    contrib_user_last_name = models.CharField(max_length=40)
    contrib_user_email = models.EmailField(unique=True)
    contrib_user_phone = models.IntegerField(unique=True)
    contrib_user_password = models.CharField(max_length=40)

    def __str__(self):
        return self.contrib_username
