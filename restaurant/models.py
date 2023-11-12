from django.db import models

# Create your models here.
class MenuTable(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    inventory = models.IntegerField()

class BookingTable(models.Model):
    name = models.CharField(max_length=11)
    no_of_guest = models.IntegerField()
    booking_date = models.DateTimeField

