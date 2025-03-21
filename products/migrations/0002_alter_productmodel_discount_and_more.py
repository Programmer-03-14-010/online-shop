# Generated by Django 5.1.6 on 2025-02-09 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='discount',
            field=models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='discount'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='image1',
            field=models.ImageField(upload_to='products', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png'])], verbose_name='image1'),
        ),
    ]
