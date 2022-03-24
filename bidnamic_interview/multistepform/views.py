from django.shortcuts import render, redirect

# import forms
from .forms import BioDataForm, BiddingInformationForm

# import generic TemplateView
from django.views.generic import TemplateView, RedirectView

#  import reverse
from django.urls import reverse, reverse_lazy

# import model to dict 
from django.forms.models import model_to_dict

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

# def get_form_data(request, step):
#     '''
#         get the form data from the session
#     '''
#     return FORM_STEPS[step]['form'](get_session_data(request, step))

def set_form_data(request, step, data):
    '''
        set form data
    '''
    request.session[SESSION_KEY_PREFIX + str(step)] = data

# get the next step count
def get_next_step(request):
    
    for i in range(1, len(FORM_STEPS)):
        # when the session is empty, assign the first step 
        if get_session_data(request, i) == None:
            return i
    return len(FORM_STEPS)


'''
    *Disclaimer*
    the repo https://github.com/jordisan/Django-multistep-form/blob/master/multistepform/views/formView.py
    was used to get  inspiration to approach the problem

'''

class MultiStepFormView(TemplateView):
    template_name = 'multistepform/bio-data-form.html'

    def get(self, request, step):
        ''' 
        when the homepage is being hit, redirect to next step to begin 
        the multi step form
        '''
        if step == None:
            step = get_next_step(request)
            return redirect(reverse('multistepform:step-parameter', kwargs={'step': step}))

        # initiate the form and pass to the template
        form = FORM_STEPS[step]['form']()

        # override context data and pass form to the template
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context=context)

    def post(self, request, step):
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

                # combine the data from the saved session data to the bidding data collected from the form
                cleaned_bidding_data.update(saved_data_in_session)

            else:
                print(form.errors)

        # for every other that is not the last 
        else:
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
                set_form_data(request, step, cleaned_data)

                # redirect to the next form step and increment the step counter
                return redirect(reverse('multistepform:step-parameter', kwargs={'step': step+1}))

            # if the bio-data form is invalid
            else:
                print(form.errors)
        

# when the clear button is hit flush the session
class ClearFormView(RedirectView):
    url = reverse_lazy('multistepform:feedback')

    def get_redirect_url(self, *args, **kwargs):
        # clear the session
        self.request.session.flush()
        return super().get_redirect_url(*args, **kwargs)

# the feedback form to start over
class FeedBackView(TemplateView):
    template_name = ''