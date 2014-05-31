import unittest
from Dish import Dish
from locu import MenuItemApiClient
from locu import VenueApiClient
import time
from Venue import Venue
global KEY 
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'


class Test(unittest.TestCase):

    def make_venue_obj(self):
        t = time.strptime("Monday 12:00:00", "%A %H:%M:%S")
        venue_client = VenueApiClient(KEY)
        v = Venue('c6c9fee9eb6fd87f176e',t)
        return v

    def test_attrs(self):
        v = self.make_venue_obj()
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
        v = self.make_venue_obj()
        v.set_menu()
        for item in v.menu:
            self.assertIsInstance(item,Dish)

    def test_menu_item_attrs(self):
        v = self.make_venue_obj()
        v.set_menu()
        menu_item = v.menu[0]
        self.assertEqual(menu_item.get_attr('price'),'1.00')
        self.assertEqual(menu_item.get_attr('name'),'Bread & Butter')
            




if __name__ == '__main__':
    unittest.main()
