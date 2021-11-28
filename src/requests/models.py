from django.db import models
from riders.models import Rider
# Create your models here.
class Request(models.Model):
    rider = models.ForeignKey(Rider, on_delete=models.CASCADE, related_name='requests')
    timestamp = models.DateTimeField(auto_now_add=True)
    source_lat = models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2)
    source_lng = models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2)
    dest_lat = models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2)
    dest_lng = models.DecimalField(max_digits=5,null=True, blank=True, decimal_places=2)