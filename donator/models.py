from datetime import datetime

from django.db import models

# Create your models here.
from django.utils import timezone

from accounts.models import CustomUser
from receiver.models import Receiver


class Donator(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)

class Donation(models.Model):
    donator = models.ForeignKey(Donator, on_delete=models.CASCADE)
    receiver = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    location_description = models.CharField(max_length=550) #the area where the donation is gonna take place
    is_approved = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)
    
