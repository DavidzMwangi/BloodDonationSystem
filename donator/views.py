from django.shortcuts import render

# Create your views here.
from donator.donatorforms import DonatorForm


def indexView(request):
    return render(request,'index.html')
def new_donor(request):
    if (request.method =='POST'):
        return 'Vee'
    else:
        form = DonatorForm()
        return render(request, 'new_receiver.html', {'form': form})
