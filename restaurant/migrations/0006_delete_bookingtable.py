# Generated by Django 4.2.7 on 2023-11-12 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_remove_bookingtable_booking_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookingTable',
        ),
    ]