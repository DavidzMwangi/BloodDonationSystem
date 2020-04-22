from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class County(models.Model):
    name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=80)


class SubCounty(models.Model):
    name = models.CharField(max_length=50)
    sub_county_code = models.CharField(max_length=80)
    county_id = models.ForeignKey(County, on_delete=models.CASCADE)


class Location(models.Model):
    name = models.CharField(max_length=50)
    location_code = models.CharField(max_length=50)
    sub_county_id = models.ForeignKey(SubCounty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    blood_group = models.CharField(max_length=50, null=False, blank=False)
    rhesus_factor = models.CharField(max_length=50, null=False, blank=False)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    class Meta:
        pass

