from locu import MenuItemApiClient
from locu import VenueApiClient
import datetime
import time

global KEY
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'


class Dish(object):

    def __init__(self,locu_object,caller,searchTime=None):
        self.venue_client = VenueApiClient(KEY)
        self.locu_object = locu_object
        self.parse_locu(self.locu_object)

        if caller == 'search':
            self.load_rating_from_id()


        elif caller == "venue":
            self.load_rating_from_venue()


    def get_attr(self,attr):
        instance_variables = self.__dict__
        return instance_variables.get(attr)


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

    def load_rating_from_id(self):
        """
        load the rating and number of ratings from database.
        """
        pass

    def load_rating_from_venue(self):
        pass
        
            




    

