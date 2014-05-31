import unittest
from Dish import Dish
from locu import MenuItemApiClient
from locu import VenueApiClient
import time
global KEY 
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'


class DishTest(unittest.TestCase):

    def makeDishobj(self):
        t = time.strptime("Monday 12:00:00", "%A %H:%M:%S")
        menu_item_client = MenuItemApiClient(KEY)
        menu_items = menu_item_client.search(locality = 'San Francisco', name = 'espresso', price__gte = 6)
        item =  menu_items['objects'][0]
        d = Dish(item,t)
        return d 




    def testAttrs(self):
        d = self.makeDishobj()
        d_attrs = d.__dict__
        espresso_attrs = {

            "name": "Espresso",
            "description": "By Illy coffee",
            "price":6,
            "id":"147a8505a445d02bc705dbc452c7c860b5f9d747439684798bdb49ef11488d0c",            
            "venue_id": "dc241e328c5cc445aea5"
        }
        for entry in espresso_attrs.keys():
            print espresso_attrs[entry],d_attrs[entry]
            self.assertEqual(espresso_attrs[entry],d_attrs[entry])



    #Sending patch to locu people to put this functionaloity in the locu api itself

    # def testCorrectTime(self):
    #     d = self.makeDishobj()
    #     self.assertEqual(d.searchTime,"12:00:00")
    #     self.assertEqual(d.searchDay,"Monday")



    # def testAvaliable(self):   
    #     d = self.makeDishobj()
    #     self.assertTrue(d.get_attr("available"))








if __name__ == '__main__':
    unittest.main()