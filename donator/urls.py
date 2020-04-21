from django.urls import path

from donator.views import indexView, new_donor
urlpatterns = [
    path('test',indexView),
    path('new_donor', new_donor, name='new_donor')
]
