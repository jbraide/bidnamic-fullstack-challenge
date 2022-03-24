# import forms from django
from django import forms

# import model
from .models import BioDataAndBiddingInformation


class BioDataForm(forms.ModelForm):
    class Meta:
        model = BioDataAndBiddingInformation
        exclude = ['bidding_setting', 'google_ads_id']

class BiddingInformationForm(forms.ModelForm):
    class Meta:
        model = BioDataAndBiddingInformation
        fields = ['bidding_setting', 'google_ads_id']


