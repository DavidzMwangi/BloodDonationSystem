from django.urls import path

from donator.views import indexView, new_donor, DonatorsView, donate, newDonation, MyDonationView

app_name = 'Donator'
urlpatterns = [
    path('test', indexView),
    path('new_donor', new_donor, name='new_donor'),
    path('donators', DonatorsView.as_view(), name='donators'),
    path('my_donations', MyDonationView.as_view(), name='my_donations'),
    path('<receiver>/donate', donate, name='donate'),
    path('new_donation', newDonation, name='new_donation')

]
