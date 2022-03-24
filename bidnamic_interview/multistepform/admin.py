from django.contrib import admin

# import models
from .models import BioDataAndBiddingInformation

@admin.register(BioDataAndBiddingInformation)
class BioDataAndBiddingInformationAdmin(admin.ModelAdmin):
    list_display = ['title', 'first_name']