# Generated by Django 3.2.19 on 2023-06-08 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0009_auto_20230606_2054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]