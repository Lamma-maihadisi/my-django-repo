# Generated by Django 4.2.7 on 2023-11-14 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BookingTable',
        ),
        migrations.AlterField(
            model_name='menutable',
            name='inventory',
            field=models.IntegerField(),
        ),
    ]