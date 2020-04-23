from django.urls import path

from receiver.views import index, new_receiver, ReceiverView

app_name = 'Receiver'
urlpatterns = [
    path('receivers', ReceiverView.as_view(), name='receivers'),
    path('new_receiver', new_receiver, name='new_receiver')

]
