from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from .models import Restaurant, MenuItem
from django.http import HttpResponse
from django.template import RequestContext


class IndexView(TemplateView):
    ### Home page.
    template_name = "index.html"
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['restaurants'] = Restaurant.objects.all()
        return context
        
class SearchView(TemplateView):
    ### Search view. Currently in testing.
    template_name = 'search.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['request'] = self.request
        context['search_term'] = self.request.GET['search']
        return context


class RestaurantView(TemplateView):
	### Restaurant Profile Page
	template_name = "restaurant.html"

	def get_context_data(self, **kwargs):
		context = super(RestaurantView, self).get_context_data(**kwargs)
		context['restaurant_name'] = context['restaurant_name'].replace('_', ' ')

		return context
    
"""
class ThrowawayView(TemplateView):
    ### Useful for testing things.
    template_name = "throwaway.html"
    """

