# import forms from django
from django import forms

# import model
from .models import BioDataAndBiddingInformation

# date field 
from django.forms.widgets import NumberInput

class BioDataForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = BioDataAndBiddingInformation
        exclude = ['bidding_setting', 'google_ads_id']

class BiddingInformationForm(forms.ModelForm):
    class Meta:
        model = BioDataAndBiddingInformation
        fields = ['bidding_setting', 'google_ads_id']


