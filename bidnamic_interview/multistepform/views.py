from django.shortcuts import render, redirect

# import forms
from .forms import BioDataForm, BiddingInformationForm

# import generic TemplateView
from django.views.generic import TemplateView



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

def get_form_data(request, step):
    '''
        get the form data from the session
    '''
    return FORM_STEPS[step]['form'](get_session_data(request, step))

def set_form_data(request, step, data):
    '''
        set form data
    '''
    request.session[SESSION_KEY_PREFIX + str(step)] = data

def get_next_step(request):
    for i in range(1, len(step)):
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
        if step == None:
            return redirect()