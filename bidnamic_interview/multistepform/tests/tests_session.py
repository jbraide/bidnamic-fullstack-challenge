from django.test import TestCase

# get the BiddingInformationForm and BioDataForm from multistep
from multistepform.forms import BiddingInformationForm, BioDataForm

# import set_form_data in session
from multistepform.views import set_form_data

# import Client
from django.test import Client

#  import date 
from datetime import date

# import request 
from django.http.request import HttpRequest

# import requestfactory
from django.test import RequestFactory

# import session middleware
from django.contrib.sessions.middleware import SessionMiddleware

# session prefix
SESSION_KEY_PREFIX = 'multistepform_step_'

class TestSessionAndView(TestCase):
    def setUp(self):
        self.client = Client()
        self.request_factory = RequestFactory()
   
    # test the data is in the session in step 1
    def test_session_availablility_for_step_1(self):

        # use the client attribute
        # browser = self.client
        
        # use request Factory
        browser = self.request_factory

        # date of birth
        date_of_birth = date(1999, 10, 10)

        form_data = {
            'title': 'Dr',
            'first_name': 'Gene',
            'last_name': 'Astrid',
            'date_of_birth': str(date_of_birth),
            'company_name': 'Build Scalable',
            'address': 'Tedek',
            'phone_number': '+2349033551708',
        }

        # send a post request to the step 1 process with the form_data
        request = browser.post('/step/1/', form_data)

        session_middleware = SessionMiddleware()
        session_middleware.process_request(request)
        # request.session.save()

        # set the form data in the session
        step_1 = SESSION_KEY_PREFIX + str(1)
        request.session[step_1] = form_data

        # get the browser session and get the dict_items 
        # (this was the way to get the session data)
        session = request.session
        session_dict_items = session.items()
        
        # construct the dict to mirror the output for session_dict_items
        step_1_dict = dict(multistepform_step_1=form_data)
        step_1_dict_items = step_1_dict.items()

        # assert that step_1_dict_items is equal to session_dict_items
        self.assertEqual(
            step_1_dict_items,
            session_dict_items,
        )
