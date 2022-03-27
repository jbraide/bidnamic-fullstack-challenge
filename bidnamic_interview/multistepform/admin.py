'''
...BiddingInformation model displayed in the admin dashboard
'''
from django.contrib import admin

# import models
from .models import BioDataAndBiddingInformation

@admin.register(BioDataAndBiddingInformation)
class BioDataAndBiddingInformationAdmin(admin.ModelAdmin):
    '''
    override the list_display attribute 
    '''
    list_display = ['title', 'first_name']
