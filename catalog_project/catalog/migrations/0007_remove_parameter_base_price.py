# Generated by Django 5.1.7 on 2025-03-30 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_rename_price_parameter_base_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameter',
            name='base_price',
        ),
    ]
