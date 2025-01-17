''' Model that represents the given structure to handle getting
    users bio-data and bidding setting
'''
from django.db import models

# import phonenumber_field
from phonenumber_field.modelfields import PhoneNumberField

class BioDataAndBiddingInformation(models.Model):
    bidding_settings = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    title = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    company_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = PhoneNumberField()
    bidding_setting = models.CharField(max_length=20, choices=bidding_settings)
    google_ads_id = models.CharField(max_length=40)
