# Generated by Django 4.0.2 on 2022-02-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NextGenQa_Contributor',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('user_first_name', models.CharField(max_length=40)),
                ('user_last_name', models.CharField(max_length=40)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_phone', models.IntegerField(unique=True)),
                ('user_password', models.CharField(max_length=40)),
                ('user_password2', models.CharField(max_length=40)),
            ],
        ),
    ]
