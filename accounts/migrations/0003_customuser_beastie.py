# Generated by Django 4.1.7 on 2023-04-23 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_registration_accepted'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='beastie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
