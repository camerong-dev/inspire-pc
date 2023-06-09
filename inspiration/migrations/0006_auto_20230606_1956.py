# Generated by Django 3.2.19 on 2023-06-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0005_auto_20230606_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManufacturerOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_manufacturer', models.CharField(max_length=150)),
                ('gpu_manufacturer', models.CharField(max_length=150)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='cpu_manufacturer',
        ),
        migrations.RemoveField(
            model_name='post',
            name='gpu_manufacturer',
        ),
    ]
