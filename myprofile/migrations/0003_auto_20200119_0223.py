# Generated by Django 2.2.6 on 2020-01-18 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myprofile', '0002_person_tue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='image',
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
