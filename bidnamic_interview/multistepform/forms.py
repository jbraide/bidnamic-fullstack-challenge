# import forms from django
from django import forms

# import model
from .models import BioDataAndBiddingInformation

# date field 
from django.forms.widgets import NumberInput

# import date
from datetime import date

class BioDataForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = BioDataAndBiddingInformation
        exclude = ['bidding_setting', 'google_ads_id']

    def clean_date_of_birth(self):
        today = date.today()
        date_of_birth = self.cleaned_data['date_of_birth']
        age = (today - date_of_birth).days / 365
        if age <= 18:
            raise forms.ValidationError('You Must be Up to 18 years')
        return date_of_birth

class BiddingInformationForm(forms.ModelForm):
    class Meta:
        model = BioDataAndBiddingInformation
        fields = ['bidding_setting', 'google_ads_id']
    
    def clean_bidding_setting(self):
        # get the tuple of bidding_settings for BioData.... Model
        bidding_settings = BioDataAndBiddingInformation.bidding_settings

        # collect the bidding setting option that was selected or inputted
        bidding_setting_option = self.cleaned_data['bidding_setting']

        # loop through the option
        for bidding_option in bidding_settings:
            if bidding_setting_option != bidding_option[0]:
                raise forms.ValidationError('This option is an Invalid Bidding Setting')
            else:
                return bidding_setting_option

