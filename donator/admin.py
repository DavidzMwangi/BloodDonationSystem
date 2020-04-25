from django.contrib import admin

# Register your models here.
from donator.models import Donator, Donation

admin.site.register(Donator)
admin.site.register(Donation)