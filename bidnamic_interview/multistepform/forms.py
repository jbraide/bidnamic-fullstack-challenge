# import forms from django
from django import forms

# import model
from .models import BioDataAndBiddingInformation

class BioDataAndBiddingInformationForm(forms.ModelForm):
    class Meta:
        model = BioDataAndBiddingInformation

class BioDataForm(BioDataAndBiddingInformationForm):
    class Meta:
        exclude = ['bidding_setting', 'google_ads_id']

class BiddingInformationForm(BioDataAndBiddingInformationForm):
    class Meta:
        fields = ['bidding_setting', 'google_ads_id']


