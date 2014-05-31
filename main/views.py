from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import RequestContext

from .models import Restaurant, MenuItem
from locu_parser.Venue import Venue
from locu_parser.Dish import Dish
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
        search_terms = {} #dict.fromkeys(['search_query', 'city', 'state', searchType])
        
        # !! Get search paramaters !! #
        if self.request.GET.get('searchType', False):
            search_terms['searchType'] = self.request.GET.get('searchType', False)
        if self.request.GET.get('searchCity', False):
            search_terms['city'] = self.request.GET.get('searchCity', False)
        if self.request.GET.get('selectState', False):
            search_terms['state'] = self.request.GET.get('selectState', False)

        if self.request.GET.get('searchQuery'):
            search_terms['search_query'] = self.request.GET['searchQuery']
            if (search_terms['searchType'] == 'restaurantSearch'):
                venues = self.venue_search(search_terms)
                context['venues'] = venues
            elif (search_terms['searchType'] == 'dishSearch'): 
                dishes = self.dish_search(search_terms)
                context['dishes'] = dishes

            context['search_terms'] = search_terms
            context['request'] = self.request
            context['search'] = self.request.GET['searchQuery']
        return context
        
    def venue_search(self, search_terms):
        venue_list = []
        t = time.strptime("Monday 12:00:00", "%A %H:%M:%S")
        venue_client = VenueApiClient(KEY)
        response = venue_client.search(locality = search_terms['city'], region = search_terms['state'], name = search_terms['search_query'])
        venues = response['objects']
        for venue_dict in venues:
            print(venue_dict)
            v = Venue(venue_dict['id'], t)
            venue_list.append(v)
        return venue_list

    def dish_search(self, search_terms):
        dish_list = []
        t = time.strptime("Monday 12:00:00", "%A %H:%M:%S")
        venue_client = VenueApiClient(KEY)
        response = venue_client.search(locality = search_terms['city'], region = search_terms['state'], name = search_terms['search_query'])
        dishes = response['objects']
        for dish_dict in dishes:
            d = Dish(dish_dict, t)
            dish_list.append(d)
        return dish_list
 
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
    template_name = "restaurant.html"

    def get_context_data(self, **kwargs):
        context = super(RestaurantView, self).get_context_data(**kwargs)
        print ('runnin get_context_data')
        venue_id = context['restaurant_name']
        print(venue_id)
        response = self.get_venue_info_and_menu(venue_id)
        return context

    def get_venue_info_and_menu(self, venue_id):
        print ("runnin")
        t = time.strptime("Monday 12:00:00", "%A %H:%M:%S")
        venue_client = VenueApiClient(KEY)
        restaurantProfile = Venue('715b3fc8c0798faf91ae', t)
        print(restaurantProfile.phone)
        print(restaurantProfile.address)
        return restaurantProfile
    
"""
class ThrowawayView(TemplateView):
    ### Useful for testing things.
    template_name = "throwaway.html"
    """

