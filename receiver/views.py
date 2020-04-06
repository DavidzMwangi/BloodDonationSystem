from django.shortcuts import render

# Create your views here.
from receiver.forms import ReceiverForm


def index(request):
    return render(request, 'receiver.html')

def new_receiver(request):
    if (request.method =='POST'):
        return 'hehe'
    else:
        form = ReceiverForm()
        return render(request, 'new_receiver.html', {'form': form})

