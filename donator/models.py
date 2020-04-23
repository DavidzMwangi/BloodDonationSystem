from django.db import models

# Create your models here.
from accounts.models import CustomUser


class Donator(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    
