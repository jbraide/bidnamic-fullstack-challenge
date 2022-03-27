# import date from datetime module
from datetime import date

# IMPORT DJANGO TESTCASE
from django.test import TestCase

# get the BiddingInformationForm and BioDataForm from multistep
from multistepform.forms import BiddingInformationForm, BioDataForm

class TestBiddingInformationForm(TestCase):
    def test_invalid_bidding_option_in_form(self):
        # this test checks form for when an invalid bidding setting option is inputted
        invalid_bidding_option = {
            'bidding_setting':'Invalid Option',
            'google_ads_id':'123-902-83727'
        }

        # Create the biddinginfoform instance and check the status by .is_valid
        bidding_form = BiddingInformationForm(invalid_bidding_option)
        validate_bidding_form = bidding_form.is_valid()
        # collect the error message and pass is as a parameter
        error_message = bidding_form.errors

        return self.assertFalse(validate_bidding_form, error_message)

    def test_valid_bidding_form(self):
        # this test checks form for when an valid bidding option is inputted
        valid_bidding_data = {
            'bidding_setting':'High',
            'google_ads_id':'123-902-83727'
        }
        bidding_form = BiddingInformationForm(valid_bidding_data)
        valid_bidding_form = bidding_form.is_valid()
        return self.assertTrue(valid_bidding_form, bidding_form.errors)

class TestBioDataForm(TestCase):
    def test_dob_under_18_requirement(self):
        # validate date entered is under 18 yrs of age.
        # get today and birthday
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
        validate_form = form.is_valid()
        return self.assertFalse(validate_form, form.errors)
    
    def test_empty_bio_data_form_field(self):
        # Empty form data
        form = BioDataForm()
        validate_form = form.is_valid()
        return self.assertFalse(validate_form)
