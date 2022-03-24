from django.test import TestCase

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
    def test_dob_under_18(self):
        return self.assertFalse()