from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from accounts.models import County, SubCounty, Location, CustomUser

admin.site.register(CustomUser, UserAdmin)
admin.site.register(SubCounty)
admin.site.register(County)
admin.site.register(Location)