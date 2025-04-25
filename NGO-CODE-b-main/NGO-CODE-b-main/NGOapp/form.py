from django import forms
from .models import *

class VolunteerForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ['full_name', 'email', 'phone', 'interests', 'photo']
        widgets = {
            'interests': forms.Textarea(attrs={'rows': 4}),
        }


from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount']
