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
    def filter_bad_results(obj_list,city,state):
        """
        filters the bad locu results
        """
        print city,state
        is_restruant =  lambda obj : all(c in  ['restaurant', 'other'] for c in obj.get_attr('categories'))
        is_in_area = lambda obj: obj.region == state
        for obj in obj_list:
            print obj.region, obj.locality
            print "in area",is_in_area(obj)
        good_venue =  lambda obj: is_restruant(obj) and is_in_area(obj)
        print filter(good_venue,obj_list)
        return filter(good_venue,obj_list)




    @staticmethod
    def venue_search(search_terms):
        venue_client = VenueApiClient(KEY)
        name = search_terms.get("search_query",'')
        city = search_terms.get("city",'')
        state = search_terms.get("state",'')
        response = venue_client.search(name=name,locality = city, region=state)["objects"]
        venues =[]
        if response:
            venues = [Venue(entry,"search") for entry in response]
            venues = Search.filter_bad_results(venues,city, state)
        return venues



    @staticmethod
    def dish_search(search_terms):
        menu_item_client= MenuItemApiClient(KEY)
        name = search_terms.get("search_query",'')
        city = search_terms.get("city",'')
        state = search_terms.get("state",'')
        response = menu_item_client.search(name=name,locality = city, region=state)["objects"]
        menu_items = []
        if response:
            menu_items = [Dish(locu_object) for locu_object in response]
            menu_items = Search.filter_bad_results(menu_items, city, state)
        return menu_items
        


