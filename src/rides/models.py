from django.db import models
from riders.models import Rider
from drivers.models import Driver
# Create your models here.
class Ride(models.Model):
    class RideOptions(models.TextChoices):
        NEW = "new","NEW"
        ACCEPTED = "accepted","ACCEPTED"
        PICKING_UP = "picking_up","PICKING_UP"
        REACHED_PICKUP = "reached_pickup","REACHED_PICKUP"
        STARTED_RIDE = "started_ride","STARTED_RIDE"
        DROPPING_OFF = "dropping_off","DROPPING_OFF"
        REACHED_DROPOFF = "reached_dropoff","REACHED_DROPOFF"
        CANCELLED = "cancelled","CANCELLED"
        COMPLETED = "completed","COMPLETED"


    driver = models.ForeignKey(Driver, blank=True, null=True,  on_delete=models.SET_NULL, related_name='rides')
    status = models.CharField(max_length=15, choices=RideOptions.choices, default=RideOptions.NEW)
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='rides')
