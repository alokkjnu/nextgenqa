# Generated by Django 4.0.2 on 2022-03-02 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nextgenqa_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nextgenqa_user',
            name='user_password2',
        ),
    ]
