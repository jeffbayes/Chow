from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Restaurant, MenuItem

class IndexView(TemplateView):
    ### Home page.
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['restaurants'] = Restaurant.objects.all()
        return context
    
"""
class ThrowawayView(TemplateView):
    ### Useful for testing things.
    template_name = "throwaway.html"
    """

