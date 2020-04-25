from django.db import models

# Create your models here.
from accounts.models import CustomUser


class Receiver(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.id}'