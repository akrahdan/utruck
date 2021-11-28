from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL
class Driver(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self) -> str:
        return self.user.username
