# Generated by Django 3.2.6 on 2021-08-10 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='email_otp',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='mobile_otp',
            field=models.IntegerField(default=0),
        ),
    ]