from django.shortcuts import render
from donator.donatorforms import DonatorForm
# Create your views here.
def indexView(request):
    return render(request,'index.html')
def new_donor(request):
    if (request.method =='POST'):
        return 'Vee'
    else:
        form = DonatorForm()
        return render(request, 'new_receiver.html', {'form': form})