# Generated by Django 3.2.19 on 2023-05-26 09:07

from django.db import migrations, models
import inspiration.formatChecker


class Migration(migrations.Migration):

    dependencies = [
        ('inspiration', '0003_auto_20230517_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='case_content',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='cpu_content',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='cpu_cooler_content',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='fans_content',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='feature_image',
            field=inspiration.formatChecker.ContentTypeRestrictedFileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='gpu_content',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='motherboard_content',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='psu_content',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='ram_content',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='secondary_image',
            field=inspiration.formatChecker.ContentTypeRestrictedFileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='storage_content',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='tertiary_image',
            field=inspiration.formatChecker.ContentTypeRestrictedFileField(upload_to=''),
        ),
    ]
