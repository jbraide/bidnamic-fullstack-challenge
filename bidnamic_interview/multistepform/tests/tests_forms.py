from django.test import TestCase

# get the BiddingInformationForm and BioDataForm from multistep
from multistepform.forms import BiddingInformationForm, BioDataForm


class TestBiddingInformationForm(TestCase):
    def test_invalid_bidding_option_in_form(self):
        invalid_bidding_option = {
            'bidding_setting':'Invalid Option',
            'google_ads_id':'123-902-83727'
        }
        bidding_form = BiddingInformationForm(invalid_bidding_option).is_valid()
        return self.assertFalse(bidding_form, 'Invalid Option selected')

    def test_valid_bidding_form(self):
        valid_bidding_data = {
            'bidding_setting':'High',
            'google_ads_id':'123-902-83727'
        }
        bidding_form = BiddingInformationForm(valid_bidding_data).is_valid()
        return self.assertTrue(bidding_form)


class TestBioDataForm(TestCase):
    # validate date entered is under 18 yrs of age.
    def test_dob_under_18_requirement(self):
        # get today and birthday
        today = date.today()
        date_of_birth = date(2020, 10, 10)

        # biodata form
        form_data = {
            'title': 'Dr',
            'first_name': 'Gene',
            'last_name': 'Astrid',
            'date_of_birth': date_of_birth,
            'company_name': 'Build Scalable',
            'address': 'Tedek',
            'phone_number': '+2349033551708',
        }
        
        form = BioDataForm(form_data)
        valid_form = form.is_valid()
        return self.assertTrue(valid_form, form.errors)