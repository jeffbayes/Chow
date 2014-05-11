from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    ### Home page.
    template_name = "index.html"

"""
class ThrowawayView(TemplateView):
    ### Useful for testing things.
    template_name = "throwaway.html"
    """

