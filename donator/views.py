from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from donator.donatorforms import DonatorForm
from donator.models import Donator, Donation

@login_required()
def indexView(request):
    return render(request,'index.html')
@login_required()
def new_donor(request):
    if (request.method =='POST'):
        return 'Vee'
    else:
        form = DonatorForm()
        return render(request, 'new_receiver.html', {'form': form})


class DonatorsView(ListView):
    template_name = 'donators.html'
    login_required =True
    def get_queryset(self):
        return Donator.objects.all()

class MyDonationView(ListView):
    login_required = True
    template_name = 'my_donations.html'

    def get_queryset(self):
        #get the current donator record
        donator = Donator.objects.filter(user=self.request.user)[1]
        return Donation.objects.get(donator=donator)