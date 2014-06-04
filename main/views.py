from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import RequestContext

from .models import DishEntry
from locu_parser.Venue import Venue
from locu_parser.Dish import Dish
from locu_parser.Search import Search
from locu import MenuItemApiClient
from locu import VenueApiClient

import datetime
import time

global KEY 
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'

class IndexView(TemplateView):
    ### Home page.
    template_name = "index.html"
        
    '''gets the data passed from index.html and creates a search request to 
    Locu API using the paramaters in the form '''
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        search_terms = {} #search_term keys: (['search_query', 'city', 'state', searchType])
        
        # !! Get search paramaters from index.html form submission!! #
        if self.request.GET.get('searchType', False):
            search_terms['searchType'] = self.request.GET.get('searchType', False)
        if self.request.GET.get('searchCity', False):
            search_terms['city'] = self.request.GET.get('searchCity', False)
        if self.request.GET.get('selectState', False):
            search_terms['state'] = self.request.GET.get('selectState', False)

        if self.request.GET.get('searchQuery'):
            search_terms['search_query'] = self.request.GET['searchQuery']
            # Search restaurants
            if (search_terms['searchType'] == 'restaurantSearch'):
                context['venues'] = Search.venue_search(search_terms)
            # search dishes
            elif (search_terms['searchType'] == 'dishSearch'): 
                context['dishes'] = Search.dish_search(search_terms)
            context['search_terms'] = search_terms
            context['request'] = self.request
            context['search'] = self.request.GET['searchQuery']
        return context
    
class RestaurantView(TemplateView):
    template_name = "restaurant.html"
    '''gets the data passed from restaurant.html and creates a venue details 
    search request to Locu API using the venue_id'''
    def get_context_data(self, **kwargs):
        context = super(RestaurantView, self).get_context_data(**kwargs)
        venue_id = context['restaurant_name']
        restaurant_profile = self.get_venue_info_and_menu(venue_id)
        context['restaurant'] = restaurant_profile
        return context

        '''requests Locu Details for restaurant giving us info like menu
        venue_id is the Locu Restaurant venue_id'''
    def get_venue_info_and_menu(self, venue_id):
        t = time.strptime("Monday 12:00:00", "%A %H:%M:%S")
        restaurant_profile = Venue(venue_id, 'venue', t)
        return restaurant_profile
    
"""
class ThrowawayView(TemplateView):
    ### Useful for testing things.
    template_name = "throwaway.html"
    """
if __name__ == '__main__':
    print "views"
