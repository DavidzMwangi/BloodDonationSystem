from django.urls import path

from donator.views import index, new_donor
urlpatterns = [
    path('test',index)
    path('new_donor', new_donor, name='new_donor')
]