from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class County(models.Model):
    name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class SubCounty(models.Model):
    name = models.CharField(max_length=50)
    sub_county_code = models.CharField(max_length=80)
    county = models.ForeignKey(County, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)
    location_code = models.CharField(max_length=50)
    sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    blood_group = models.CharField(max_length=50, null=False, blank=False)
    rhesus_factor = models.CharField(max_length=50, null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)

    class Meta:
        pass
    def __str__(self):
        return self.username

