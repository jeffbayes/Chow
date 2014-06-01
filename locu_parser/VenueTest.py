import unittest
from Dish import Dish
from locu import MenuItemApiClient
from locu import VenueApiClient
import time
from Venue import Venue
global KEY 
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'


class Test(unittest.TestCase):



    def make_obj_by_search(self):
        venue_client = VenueApiClient(KEY)
        venue_response = venue_client.search(name="Taqueria Belly",locality='eugene',region='OR')["objects"][0]
        v  =  Venue(venue_response,"search")
        return v

    def make_obj_by_venue(self):
        t = time.strptime("Monday 12:00:00", "%A %H:%M:%S")
        v = Venue('c6c9fee9eb6fd87f176e','venue',t)
        return v

    def test_by_venue(self):
        v = self.make_obj_by_venue()
        v_attrs = v.__dict__
        belly_attrs = {

            "name": "Taqueria Belly",
            "address": "291 E. 5th Ave.",
            "lat": 44.054394,
            "long": -123.089083,
            "phone": "(541) 687-8226",
            "venue_id": "c6c9fee9eb6fd87f176e"
        }
        for entry in belly_attrs.keys():
            print belly_attrs[entry],v_attrs[entry]
            self.assertEqual(belly_attrs[entry],v_attrs[entry])

    def test_by_search(self):
        v = self.make_obj_by_search()
        v_attrs = v.__dict__
        belly_attrs = {

            "name": "Taqueria Belly",
            "address": "291 E. 5th Ave.",
            "lat": 44.054394,
            "long": -123.089083,
            "phone": "(541) 687-8226",
            "venue_id": "c6c9fee9eb6fd87f176e"
        }
        for entry in belly_attrs.keys():
            print belly_attrs[entry],v_attrs[entry]
            self.assertEqual(belly_attrs[entry],v_attrs[entry])


    def test_menu_item_class(self):
        v = self.make_obj_by_venue()
        for item in v.menu:
            self.assertIsInstance(item,Dish)

    def test_menu_item_attrs(self):
        v = self.make_obj_by_venue()
        menu_item = v.menu[0]
        self.assertEqual(menu_item.get_attr('price'),'1.00')
        self.assertEqual(menu_item.get_attr('name'),'Bread & Butter')
            




if __name__ == '__main__':
    unittest.main()
