from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView

from donator.donatorforms import DonatorForm
from donator.models import Donator, Donation
from receiver.models import Receiver


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

def donate(request,receiver):
    receiver = Receiver.objects.get(pk=receiver)
    return render(request,'donate.html',{
        'receiver':receiver,
        'current_date':datetime.now()
    })

@login_required()
def newDonation(request):
    if request.method =='POST':
        
        request_data=request.POST.dict()
        receiver = Receiver.objects.get(pk=request_data.get('receiver_id'))
        
        try:
            donator = Donator.objects.get(user=request.user)
        except Donator.DoesNotExist:
            donator = Donator()
            donator.user=request.user
            donator.description="Sample Description"
            donator.save()
            
        donation = Donation()
        donation.receiver=receiver
        donation.donator=donator
        donation.location_description = request_data.get("location_description")
        donation.date = datetime.now()
        donation.save()

        return reverse_lazy('Donator:my_donations')
    else:
        print("Method not allowed")

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
        donator = Donator.objects.get(user=self.request.user)
        return Donation.objects.filter(donator=donator)

