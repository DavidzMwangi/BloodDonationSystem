from django import forms

from accounts.models import CustomUser
from receiver.models import Receiver


class ReceiverForm(forms.ModelForm):
    user_id = forms.ModelChoiceField(CustomUser.objects.all())
    description = forms.CharField(label='Enter the description of the receiver', max_length=250)

    class Meta:
        model = Receiver
        fields = ('user_id', 'description')
