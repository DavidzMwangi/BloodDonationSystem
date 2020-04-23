from django.urls import path

from donator.views import indexView, new_donor, DonatorsView
app_name = 'Donator'
urlpatterns = [
    path('test', indexView),
    path('new_donor', new_donor, name='new_donor'),
    path('donators', DonatorsView.as_view(), name='donators')
]
