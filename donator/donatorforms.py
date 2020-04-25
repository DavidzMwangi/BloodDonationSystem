from django import forms
from accounts.models import CustomUser
from donator.models import Donator

class DonatorForm(forms.ModelForm):
    user_id = forms.ModelChoiceField(CustomUser.objects.all())
    description = forms.CharField(label='Enter the description of the donor', max_length=250)

    class Meta:
        model = Donator
        fields = ('user_id', 'description')

