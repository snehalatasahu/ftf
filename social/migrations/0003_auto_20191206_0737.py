# Generated by Django 2.2.6 on 2019-12-06 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20190716_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='myprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='myprofile',
            name='phone_no',
        ),
        migrations.RemoveField(
            model_name='myprofile',
            name='status',
        ),
    ]
