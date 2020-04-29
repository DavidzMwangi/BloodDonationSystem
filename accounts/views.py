from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
# Create your views here.
from django.template import context
from django.views.generic import TemplateView

from accounts.forms import RegisterForm
from donator.models import Donator
from receiver.models import Receiver


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # save user depending on if the user type
            user = authenticate(username=username, password=password)
            login(request, user)

            # determine if user is a donator or a receiver
            if (form.cleaned_data.get('user_type') == 0):
                # donator
                donator = Donator()
                donator.description = form.cleaned_data.get('description')
                donator.user = user
                donator.save()
            else:
                # receiver
                receiver = Receiver()
                receiver.description = form.cleaned_data.get('description')
                receiver.user = user
                receiver.save()

            return redirect('Accounts:user_dashboard')
        else:
            print("error")
            print(form.errors)


    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


class DashboardView(TemplateView):
    login_required = True
    template_name = "admin_dashboard.html"
    donators = Donator.objects.count()
    receivers = Receiver.objects.count()



    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context.update({'donators': self.donators, 'receivers': self.receivers})
        return context


class DonatorReceiverDashboardView(TemplateView):
    login_required = True
    template_name = 'donator_receiver_dashboard.html'

    donators = Donator.objects.count()
    receivers = Receiver.objects.count()

    def get_context_data(self, **kwargs):
        context = super(DonatorReceiverDashboardView, self).get_context_data(**kwargs)
        context.update({'donators': self.donators, 'receivers': self.receivers})
        return context


def loginRequest(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.is_superuser:
                # admin
                return redirect('Accounts:dashboard')
            else:
                # //receiver/donator
                return redirect('Accounts:user_dashboard')
        else:
            return render(request, 'login.html', {'error': 'The user does not exist, please register'})


    else:

        return render(request, 'login.html', {'error': 'An error occurred'})
