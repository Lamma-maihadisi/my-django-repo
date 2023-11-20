from django.db import models
from django.utils import timezone

# Create your models here.
class MenuTable(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    inventory = models.IntegerField()
    

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField(default=1)
    booking_date = models.DateTimeField()