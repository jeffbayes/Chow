from locu import MenuItemApiClient
from locu import VenueApiClient
from main.models import DishEntry
import datetime
import time

global KEY
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'


class Dish(object):

    def __init__(self,caller,locu_object ='',searchTime='',**attrs):
        self.venue_client = VenueApiClient(KEY)
        self.locu_object = locu_object
        self.parse_locu(self.locu_object)

        if caller == 'search':
            self.load_rating_from_id()


        elif usage == "menu":
            self.load_rating_from_venue()


    def get_attr(self,attr):
        self.attrs.get(attr,"Data Not Available")



    def parse_locu(self,locu_object):
        """
        Takes Locu Object and creates attributes dictonary.

        args:  
            locu_object: a json style dict with dish information
        """
        self.name = self.locu_object.get("name")
        self.description = self.locu_object.get("description")
        self.price = self.locu_object.get("price")
        self.venue = self.locu_object["venue"].get("name")
        self.venue_id = self.locu_object["venue"].get("id")
        self.id = self.locu_object.get("id")

        details = self.venue_client.get_details(self.locu_object["venue"]["id"])

        # if self.searchDay:
        #     hours_today = details["objects"][0]["open_hours"][self.searchDay]
        #     if hours_today:        
        #         self.attrs["available"] = LocuHelper.isOpen(hours_today,self.searchTime)


    def load_rating_from_id(self):
        """
        load the rating and number of ratings from database.
        """
        pass

    def load_rating_from_venue(self):
        pass
        
            



if __name__ == '__main__':
    # dish = Dish()
    venue_client = VenueApiClient(KEY)
    menu_item_client = MenuItemApiClient(KEY)
    menu_items = menu_item_client.search(locality = 'San Francisco', name = 'espresso', price__gte = 6)  
    item =  menu_items['objects'][0]
    venueID = item["venue"]["id"]
    details = venue_client.get_details('dc241e328c5cc445aea5')
    # hours = details["objects"][0]["open_hours"]["Monday"]
    # dish.parse_open_hours(hours)



    

