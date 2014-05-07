from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    """ Home page. """
    template_name = "index.html"
