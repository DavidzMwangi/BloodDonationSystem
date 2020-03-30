from django.db import models

# Create your models here.
from accounts.models import CustomUser


class Donator(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
