from django.test import TestCase

# import BioData.... Model
from multistepform.models import BioDataAndBiddingInformation

#  import date 
from datetime import date

# import User model
from django.contrib.auth.models import User

# import Client
from django.test import Client

class ViewAllRecords(TestCase):
    def setUp(self):
        # create a new user Record
        User.objects.create(
            username='testing',
            email='testing@gmail.com',
            password='GcHPuBB@c$$@m4Mp'
        )

        model = BioDataAndBiddingInformation

        # create some records
        model.objects.create(
            title='Hon',
            first_name='Joseph',
            surname='Braide',
            date_of_birth=date(1996,10,10),
            company_name='Build Scalable',
            address='Mbong Peters Close',
            phone_number='+2349033551708',
            bidding_setting='High',
            google_ads_id='123-456-7890'
        )

        model.objects.create(
            title='Dr',
            first_name='Benjamin',
            surname='Carson',
            date_of_birth=date(1951,9,18),
            company_name='University of Michigan Medical School',
            address='Fake Address United states',
            phone_number='+12025550198',
            bidding_setting='Medium',
            google_ads_id='123-456-7890'
        )

        model.objects.create(
            title='Mr',
            first_name='Thomas',
            surname='Edison',
            date_of_birth=date(1847,2,11),
            company_name='Edison Electric Company',
            address='Menlo Park',
            phone_number='+12025550198',
            bidding_setting='High',
            google_ads_id='123-456-7890'
        )

        self.client = Client()

        self.model = model

    def test_to_view_all_applications(self):
        # create a variable of the client
        browser = self.client

        # get the user
        user = User.objects.get(
            username='testing'
        )

        # login user
        browser.force_login(
            user
        )

        # response from the browser
        response = browser.get('/view-applications/')

        # get all the applications created
        applications_query = self.model.objects.values(
            'id', 
            'title', 
            'first_name', 
            'surname', 
            'date_of_birth', 
            'date_of_birth', 
            'company_name', 
            'bidding_setting', 
            'google_ads_id')
        
        context = response.context['all_applications']

        # assert the right amount of records are displaying
        self.assertEqual(len(context), 3)

        # assert the context data is equal to the query
        # self.assertEqual(context, applications_query)


        
