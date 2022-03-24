from django.shortcuts import render

# import forms
from .forms import BioDataForm, BiddingInformationForm

# import generic TemplateView
from django.views.generic import TemplateView

'''
    *Disclaimer*
    the repo https://github.com/jordisan/Django-multistep-form/blob/master/multistepform/views/formView.py
    was used to get  inspiration to approach the problem

'''

class MultiStepFormView(TemplateView):
    template_name = 'multistepform/bio-data-form.html'

    # def get(self, request, step):
    #     if step == None:
    #         return redirect()