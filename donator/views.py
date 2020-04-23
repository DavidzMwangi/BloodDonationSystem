from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from donator.donatorforms import DonatorForm
from donator.models import Donator


def indexView(request):
    return render(request,'index.html')
def new_donor(request):
    if (request.method =='POST'):
        return 'Vee'
    else:
        form = DonatorForm()
        return render(request, 'new_receiver.html', {'form': form})

class DonatorsView(ListView):
    template_name = 'donators.html'

    def get_queryset(self):
        return Donator.objects.all()
