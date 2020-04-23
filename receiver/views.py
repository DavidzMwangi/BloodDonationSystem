from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from receiver.forms import ReceiverForm
from receiver.models import Receiver


def index(request):
    return render(request, 'receivers.html')

def new_receiver(request):
    if (request.method =='POST'):
        return 'hehe'
    else:
        form = ReceiverForm()
        return render(request, 'new_receiver.html', {'form': form})

class ReceiverView(ListView):
    template_name = 'receivers.html'
    def get_queryset(self):
        return Receiver.objects.all()
