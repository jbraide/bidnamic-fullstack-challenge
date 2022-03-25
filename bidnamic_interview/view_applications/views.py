from django.shortcuts import render

# import BioDataAndBiddingInformation model
from multistepform.models import BioDataAndBiddingInformation

# import TemplateView
from django.views.generic import TemplateView, RedirectView

# import reverse_lazy 
from django.urls import reverse_lazy

# import success Message
from django.contrib.messages import success


class ViewAllApplications(TemplateView):
    template_name = 'view_applications/view-applications.html'
    model = BioDataAndBiddingInformation

    # override get_context data
    def get_context_data(self, **kwargs):
        bio_data_bidding_information_query = self.model.objects.values(
            'id', 
            'title', 
            'first_name', 
            'surname', 
            'date_of_birth', 
            'date_of_birth', 
            'company_name', 
            'bidding_setting', 
            'google_ads_id')
        kwargs['all_applications'] = bio_data_bidding_information_query
        return super().get_context_data(**kwargs)


class RemoveApplicationRecord(RedirectView):
    url = reverse_lazy('view-applications:all-applications')

    def get_redirect_url(self, *args, **kwargs):
        record_id = kwargs['id']
        BioDataAndBiddingInformation.objects.get(id=record_id).delete()
        success(self.request, 'Successfully Removed')
        return super().get_redirect_url(*args, **kwargs)
