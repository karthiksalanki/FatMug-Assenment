# Generated by Django 4.2.7 on 2023-11-22 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vm_app', '0003_alter_performance_average_response_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='average_response_time',
            field=models.FloatField(),
        ),
    ]
