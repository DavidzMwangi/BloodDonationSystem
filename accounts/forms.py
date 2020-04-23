from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import CustomUser, Location

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email Address', max_length=200)
    phone_number = forms.CharField(label='Phone Number', max_length=10)
    blood_group = forms.CharField(label='Blood Group', max_length=100)
    rhesus_factor = forms.CharField(label="Rhesus Factor", max_length=250)
    location_id = forms.ModelChoiceField(queryset=Location.objects.all())

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'blood_group', 'rhesus_factor', 'location_id')

class LoginForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=30)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        