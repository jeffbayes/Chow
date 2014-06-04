from locu import MenuItemApiClient
from locu import VenueApiClient
from Dish import Dish
import datetime
import time
global KEY
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'

class Venue(object):

    def __init__(self,locu_info,caller,searchTime=None):
        """
        If caller is a search locu_info will just be a 
        json dict if it's a venue it'll be a venue  id

        this is to prevent making a ton of venue detail calls
        """
        self.venue_client = VenueApiClient(KEY)
        self.caller = caller
        self.menu = [] ## Filled by set_menu()

        if caller == 'search':
            self.locu_object = locu_info
        elif caller == "venue":
            self.locu_object = self.venue_client.get_details(locu_info)["objects"][0]

        self.set_attrs(caller)
        
        if searchTime:
            self.searchTime = time.strftime( "%H:%M:%S",searchTime)
            self.searchDay = time.strftime("%A",searchTime)
       

        
    def get_attr(self,attr):
        instance_variables = self.__dict__
        return instance_variables.get(attr)


    def set_attrs(self,caller):
        """
        Sets the Venue attrs. It will only set the menu if the caller is a venue page.
        This is for two reasons:
            a) to avoid extraneous venue detail calls
            b) the locu_object will be a json style dict that won't have a menu entry
        """
        dna = "Data Not Available"
        self.name = self.locu_object.get("name",dna)
        self.address = self.locu_object.get("street_address",dna)
        self.postal_code = self.locu_object.get("postal_code",dna)
        self.locality = self.locu_object.get("locality",dna)
        self.region = self.locu_object.get("region",dna)
        self.phone = self.locu_object.get("phone",dna)
        self.venue_id = self.locu_object.get("id",dna)
        self.lat = self.locu_object.get("lat",dna)
        self.long = self.locu_object.get("long",dna)
        self.has_menu = self.locu_object.get("has_menu",dna)
        self.categories = self.locu_object.get("categories")

        if self.has_menu and caller=='venue':
            self.set_menu()

        # if self.searchDay:
        #     hours_today = details["objects"][0]["open_hours"][self.searchDay]
        #     if hours_today:        
        #         self.attrs["available"] = LocuHelper.isOpen(hours_today,self.searchTime)

    def set_menu(self):
        """
        Parse the locu json and creates a list of Dish objects
        Must be called when venue page is loaded. We don't do it in the init
        so we don't have to parse a menu for all the venues in a query.
        """
        for menu in self.locu_object["menus"]:
            for section in menu["sections"]:
                for sub_section in section["subsections"]:
                    for item in sub_section["contents"]:
                        item["venue"] = self.locu_object
                        if item["type"] == "ITEM":
                            dish = Dish(item,'venue')
                            self.menu.append(dish)
if __name__ == '__main__':
    pass
    