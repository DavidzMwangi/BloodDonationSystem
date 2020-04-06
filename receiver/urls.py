from django.urls import path

from receiver.views import index, new_receiver

app_name = 'Receiver'
urlpatterns = [
    path('test', index),
    path('new_receiver', new_receiver, name='new_receiver')

]
