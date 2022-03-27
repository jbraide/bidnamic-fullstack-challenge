'''
*Disclaimer*
the repo https://github.com/jordisan/Django-multistep-form/blob/master/multistepform/views/formView.py
was used to get  inspiration to approach the problem
'''
from django.shortcuts import redirect

# import generic TemplateView
from django.views.generic import TemplateView

#  import reverse
from django.urls import reverse, reverse_lazy

# import forms
from .forms import BioDataForm, BiddingInformationForm

# import model
from .models import BioDataAndBiddingInformation

'''
    Define session key prefix and add Bio Data and BiddingInfo. form data to
    FORM_STEPS dictionary
'''
SESSION_KEY_PREFIX = 'multistepform_step_'

FORM_STEPS = {
    1: {
        'form': BioDataForm
    },
    2: {
        'form': BiddingInformationForm
    }
}

'''
    functions to handle
    - getting the session
    - getting form data from the session
    - add form data to the session
'''

def get_session_data(request, step):
    '''
        get session data by concatenate Prefix and add to the step as * suffix *
    '''
    return request.session.get(SESSION_KEY_PREFIX + str(step))

def set_form_data(request, step, data):
    '''
        set form data
    '''
    request.session[SESSION_KEY_PREFIX + str(step)] = data

# get the next step count
def get_next_step(request):
    for i in range(1, len(FORM_STEPS)):
        # when the session is empty, assign the first step
        if get_session_data(request, i) is None:
            return i
    return len(FORM_STEPS)


class MultiStepFormView(TemplateView):
    '''
    Implements the multistep wizard logic for
    1. collecting biodata into the session as the first step
    2. collecting the bidding setting and google_ads_id from the form
    3. storing the entire record in one model class BioDataAndBiddingInformation
    '''
    template_name = 'multistepform/bio-data-form.html'

    def get(self, request, step, *args, **kwargs):
        '''
        Override the default get method to pass multistep form and step to
        the template
        '''
        # when the homepage is being hit, redirect to next step to begin the multi step form
        if step is None:
            step = get_next_step(request)
            return redirect(reverse('multistepform:step-parameter', kwargs={'step': step}))

        # initiate the form and pass to the template
        form = FORM_STEPS[step]['form']()

        # override context data and pass form to the template
        context = self.get_context_data(**kwargs)
        context['form'] = form
        context['step'] = step

        return self.render_to_response(context=context)

    def post(self, request, step, **kwargs):
        '''
        Handles the process for each form step
        - 
        '''
        context = self.get_context_data(**kwargs)

        # get the current step and let it accept a POST request
        form = FORM_STEPS[step]['form'](request.POST)

        # if at the last step
        if step == len(FORM_STEPS):
            # if the form is valid
            if form.is_valid():
                # collect the bidding data from the form
                cleaned_bidding_data = form.cleaned_data

                # loop through the session data
                for i in range(1, len(FORM_STEPS)):
                    saved_data_in_session = get_session_data(request, i)

                # combine the data from the saved session data to the bidding
                # data collected from the form
                cleaned_bidding_data.update(saved_data_in_session)

                # create the biodataandbidding record and flush the session
                BioDataAndBiddingInformation(**cleaned_bidding_data).save()

                request.session.flush()

                return redirect(reverse('multistepform:feedback', kwargs={'heading': 'Submitted', 'message': 'The session has been successfully cleared'}))
            context['form'] = form
            return self.render_to_response(context=context)

        # for every other that is not the last
        # if the bio-data form is valid
        if form.is_valid():

            # get the forms cleaned data
            cleaned_bio_data = form.cleaned_data

            '''
                convert dob and phone no to strings to remove errors
                - Object of type datet is not JSON serializable
                - Object of type phone_number is not JSON serializable
            '''
            date_of_birth = str(cleaned_bio_data['date_of_birth'])
            phone_numbers = str(cleaned_bio_data['phone_number'])

            # update the values
            cleaned_bio_data['date_of_birth'] = date_of_birth
            cleaned_bio_data['phone_number'] = phone_numbers

            # set the form data to the session
            set_form_data(request, step, cleaned_bio_data)

            # redirect to the next form step and increment the step counter
            return redirect(reverse('multistepform:step-parameter', kwargs={'step': step+1}))

        context['form'] = form
        return self.render_to_response(context=context)

# when the clear button is hit flush the session
class ClearFormView(TemplateView):
    template_name = 'multistepform/feedback.html'

    def get(self, *args, **kwargs):
        # clear the session
        self.request.session.flush()
        return redirect(reverse_lazy('multistepform:feedback',
        kwargs={'heading': 'Cleared', 'message': 'The session has been successfully cleared'}
        ))

# the feedback form to start over
class FeedBackView(TemplateView):
    template_name = 'multistepform/feedback.html'
