# Generated by Django 4.1.1 on 2022-09-16 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_stages_authenticator_duo", "0003_duodevice_last_t"),
    ]

    operations = [
        migrations.AddField(
            model_name="authenticatorduostage",
            name="admin_integration_key",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="authenticatorduostage",
            name="admin_secret_key",
            field=models.TextField(blank=True, default=""),
        ),
    ]
