from locu import MenuItemApiClient
from locu import VenueApiClient
from Dish import Dish
import datetime
import time
global KEY
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'

class Venue(object):

    def __init__(self,venue_id,searchTime=None):
        self.venue_client = VenueApiClient(KEY)
        self.locu_object = self.venue_client.get_details(venue_id)["objects"][0]
        self.set_attrs()
        
        if searchTime:
            self.searchTime = time.strftime( "%H:%M:%S",searchTime)
            self.searchDay = time.strftime("%A",searchTime)
        self.menu = [] ## Filled by set_menu()

        
    def get_attr(self,attr):
        if attr in self.attrs:
            return self.attrs[attr]
        else:
            return "Data Not Available"



    def set_attrs(self):
        """
        Sets the Venue attrs
        """
        dna = "Data Not Available"
        self.name = self.locu_object.get("name",dna)
        self.address = self.locu_object.get("street_address",dna)
        self.phone = self.locu_object.get("phone",dna)
        self.venue_id = self.locu_object.get("id",dna)
        self.lat = self.locu_object.get("lat",dna)
        self.long = self.locu_object.get("long",dna)
        self.has_menu = self.locu_object.get("has_menu",dna)
        self.categories = self.locu_object.get("categories")
        if self.has_menu:
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
    venue_client = VenueApiClient(KEY)
    venue_items = venue_client.search(locality = 'Eugene',region="OR", name = 'Belly')
    item =  venue_items['objects'][0]
    v = Venue(item)
    v.set_menu()
    for i in range(50): print
    d = v.menu[0]
    print d.get_attr('venue')


    

