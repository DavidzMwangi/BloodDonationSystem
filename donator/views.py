from django.shortcuts import render
<<<<<<< HEAD
from donator.donatorforms import DonatorForm
=======
>>>>>>> ef05274d9974aa58cbd382230deb731a308a8d5c
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
