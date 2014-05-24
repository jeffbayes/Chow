from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import RequestContext

from .models import Restaurant, MenuItem
from .parsers import Venue, Dish
from locu import MenuItemApiClient
from locu import VenueApiClient

import datetime
import time

global KEY 
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'

class IndexView(TemplateView):
    ### Home page.
    template_name = "index.html"
    
    """
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['restaurants'] = Restaurant.objects.all()
        return context
    """
        
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        search_terms = {} #dict.fromkeys(['restaurant', 'city', 'state'])
        if self.request.GET.get('searchCity', False):
            search_terms['city'] = self.request.GET.get('searchCity', False)
        
        print("Does state exist?: ", self.request.GET.get('selectState', False))

        if self.request.GET.get('selectState', False):
            search_terms['state'] = self.request.GET.get('selectState', False)
        if self.request.GET.get('searchRestaurant'):
            search_terms['restaurant'] = self.request.GET['searchRestaurant']
            venues = self.venue_search(search_terms)
            context['venues'] = venues
            context['request'] = self.request
            context['search'] = self.request.GET['searchRestaurant']

        
        return context
        
    def venue_search(self, search_terms):
        venue_list = []
        t = time.strptime("Monday 12:00:00", "%A %H:%M:%S")
        venue_client = VenueApiClient(KEY)
        print ("Printing search term: ", search_terms)
        response = venue_client.search(locality = search_terms['city'], region = search_terms['state'], name = search_terms['restaurant'])
        venues = response['objects']
        for venue_dict in venues:
            v = Venue(venue_dict, t)
            venue_list.append(v)
        return venue_list
 
"""       
class RestaurantSearchView(TemplateView):
    ### Restaurant search view. Currently in testing.
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        search_term = self.request.GET['search']
        if search_term:
            venues = venue_search(search_term)
            venues['query_match'] = venues['objects']
            context['request'] = self.request
            context['search'] = self.request.GET['search']
        return context
        
    def venue_search(search_term):
        t = time.strptime("Monday 12:00:00", "%A %H:%M:%S")
        venue_client = VenueApiClient(KEY)
        venues = venue_client.search(locality = 'Eugene', name = search_term)  
        return venues
"""


class RestaurantView(TemplateView):
	### Restaurant Profile Page
	template_name = "restaurant.html"

	"""def get_context_data(self, **kwargs):
		context = super(RestaurantView, self).get_context_data(**kwargs)
        venue_id = context['restaurant_name']
        return context"""
    
"""
class ThrowawayView(TemplateView):
    ### Useful for testing things.
    template_name = "throwaway.html"
    """

