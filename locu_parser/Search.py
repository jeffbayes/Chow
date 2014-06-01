from locu import MenuItemApiClient
from locu import VenueApiClient
from Venue import Venue
from Dish import Dish

global KEY
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'


class Search(object):

    def __init__(self):
        pass

    @staticmethod
    def venue_search(search_terms):
        venue_client = VenueApiClient(KEY)
        name = search_terms.get("name",'')
        city = search_terms.get("city",'')
        state = search_terms.get("state",'')
        response = venue_client.search(name=name,locality = city, region=state)["objects"]
        venues =[]
        if response:
            venues = [Venue(entry,"search") for entry in response]
            not_restruant = lambda venue: not(any(x in venue.categories for x in ['restaurant', 'other']))
            filter(not_restruant,venues)
        return venues



    @staticmethod
    def dish_search(search_terms):
        menu_item_client= MenuItemApiClient(KEY)
        name = search_terms.get("name",'')
        city = search_terms.get("city",'')
        state = search_terms.get("state",'')
        response = menu_item_client.search(name=name,locality = city, region=state)["objects"]
        menu_items = []
        if response:
            menu_items = [Dish(locu_object) for locu_object in response]
        print type(menu_items)
        return menu_items

        


