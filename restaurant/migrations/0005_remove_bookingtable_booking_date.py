# Generated by Django 4.2.7 on 2023-11-12 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_bookingtable_booking_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingtable',
            name='booking_date',
        ),
    ]
