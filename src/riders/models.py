from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL
# Create your models here.
class Rider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()

    def __str__(self) -> str:
        return self.user.username
