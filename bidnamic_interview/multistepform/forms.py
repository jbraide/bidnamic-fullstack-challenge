# import date
from datetime import date
# import forms from django
from django import forms
# date field
from django.forms.widgets import NumberInput

# import model
from .models import BioDataAndBiddingInformation

# form representation for Biodata and Bidding setting
class BioDataForm(forms.ModelForm):
    '''
    - BioDataForm excludes the bidding_setting and google_ads_id from the
    model as it has nothing to do with getting the users information
    - Provides a clean method for date_of_birth to check for users not older than 18 years
    '''
    date_of_birth = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = BioDataAndBiddingInformation
        exclude = ['bidding_setting', 'google_ads_id']

    def clean_date_of_birth(self):
        '''Provides a clean method for date_of_birth to check for users not older than 18 years'''
        today = date.today()
        date_of_birth = self.cleaned_data['date_of_birth']
        age = (today - date_of_birth).days / 365
        if age < 18:
            raise forms.ValidationError('You Must be Up to 18 years')
        return date_of_birth

class BiddingInformationForm(forms.ModelForm):
    '''
    - BiddingInformation excludes the others related with getting the users information,
    being focused on collecting the Users bidding choices and gogole_ads_id
    '''
    class Meta:
        model = BioDataAndBiddingInformation
        fields = ['bidding_setting', 'google_ads_id']
    def clean_bidding_setting(self):
        '''
        - Provides a clean method for checking an invalid option made by the user
        (checked while unit testing)
        '''
        # get the tuple of bidding_settings for BioData.... Model
        bidding_settings = BioDataAndBiddingInformation.bidding_settings

        # collect the bidding setting option that was selected or inputted
        bidding_setting_option = self.cleaned_data['bidding_setting']

        # loop through the option
        for bidding_option in bidding_settings:
            # if the bidding setting option is not one of the options raise the following error....
            if bidding_setting_option != bidding_option[0]:
                raise forms.ValidationError('This option is an Invalid Bidding Setting')
            
            # return the bidding setting option from the form
            else:
                return bidding_setting_option
