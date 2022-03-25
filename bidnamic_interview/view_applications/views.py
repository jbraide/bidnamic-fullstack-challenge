from django.shortcuts import render

# import BioDataAndBiddingInformation model
from multistepform.models import BioDataAndBiddingInformation

# import TemplateView
from django.views.generic import TemplateView


class ViewAllApplications(TemplateView):
    template_name = 'view_applications/view-applications.html'
    model = BioDataAndBiddingInformation

    # override get_context data
    def get_context_data(self, **kwargs):
        bio_data_bidding_information_query = self.model.objects.values('title', 'first_name', 'surname', 'date_of_birth', 'date_of_birth', 'company_name', 'bidding_setting', 'google_ads_id')
        kwargs['all_applications'] = bio_data_bidding_information_query
        return super().get_context_data(**kwargs)
