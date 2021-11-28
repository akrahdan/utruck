from django.db import models
from drivers.models import Driver
# Create your models here.

class Vehicle(models.Model):
    owner = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name="vehicles")
    vehicle_model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.vehicle_model
