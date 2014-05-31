from locu import MenuItemApiClient
from locu import VenueApiClient


global KEY
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'


class Search(object):

    def __init__(self):
        pass

    @staticmethod
    def venue_search(name,city='',state=''):
        venue_client = VenueApiClient(KEY)
        results = venue_client.search(name=name,locality = city, region=state)
        venues =[]
        if results["objects"]:
            venues = [Venue(result["id"]) for result in results]
            not_restruant = lambda venue: not(any(x in Venue.categories for x in ['restaurant', 'other']))
            filter(not_restruant,venues)
        return venues


    def search_dishes(name,city='',state=''):
        menu_item_client= MenuItemApiClient(KEY)
        results = menu_item_client.search(name=name,locality = city, region=state)
        


