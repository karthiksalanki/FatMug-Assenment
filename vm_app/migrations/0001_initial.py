# Generated by Django 4.2.7 on 2023-11-20 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_details', models.TextField()),
                ('address', models.TextField()),
                ('vendor_code', models.CharField(max_length=25)),
                ('on_time_delivery_rate', models.FloatField(default=0)),
                ('quality_rating_avg', models.FloatField(default=0)),
                ('average_response_time', models.FloatField(default=0)),
                ('fulfillment_rate', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'Vendor',
                'verbose_name_plural': 'Vendor',
            },
        ),
        migrations.CreateModel(
            name='Purchase_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('po_number', models.CharField(max_length=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateTimeField()),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'pending'), ('completed', 'completed'), ('canceled', 'canceled')], default='pending', max_length=10)),
                ('quality_rating', models.FloatField()),
                ('issue_date', models.DateTimeField(blank=True, null=True)),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vm_app.vendor')),
            ],
            options={
                'verbose_name': 'Purchase Order',
                'verbose_name_plural': 'Purchase Order',
            },
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('on_time_delivery_rate', models.FloatField()),
                ('quality_rating_avg', models.FloatField()),
                ('average_response_time', models.FloatField()),
                ('fulfillment_rate', models.FloatField()),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='vm_app.vendor')),
            ],
            options={
                'verbose_name': 'Purchase Order',
                'verbose_name_plural': 'Purchase Order',
            },
        ),
    ]
