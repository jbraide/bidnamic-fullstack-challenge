# import forms from django
from django import forms

# import model
from .models import BioDataAndBiddingInformation

# date field 
from django.forms.widgets import NumberInput

# import date
from datetime import date, timedelta

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


