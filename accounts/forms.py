from django.contrib.auth.forms import UserCreationForm
from django import forms

from accounts.models import CustomUser, Location

USER_TYPES = [
    (0, 'Donator'),
    (1, 'Receiver')
]

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email Address', max_length=200)
    phone_number = forms.CharField(label='Phone Number', max_length=10)
    blood_group = forms.CharField(label='Blood Group', max_length=100)
    rhesus_factor = forms.CharField(label="Rhesus Factor", max_length=250)
    location_id = forms.ModelChoiceField(queryset=Location.objects.all())
    user_type = forms.IntegerField(widget=forms.Select(choices=USER_TYPES))
    description = forms.CharField(label='Description', max_length=550)
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'blood_group', 'rhesus_factor', 'location_id','user_type', 'description')

