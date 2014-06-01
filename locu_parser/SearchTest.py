import unittest
from Search import Search

class SearchTest(unittest.TestCase):

    def test_venue_search(self):
    	search_terms = {"name":"belly","city":"eugene","state":"OR"}
        venues = Search.venue_search(search_terms)
        names =[ "Belly","Taqueria Belly"]
        venue_names = [venue.name for venue in venues]
        self.assertEqual(names.sort(),venue_names.sort())

    def test_dish_search(self):
    	search_terms = {"name":"gumbo","city":"eugene","state":"OR"}
    	dishes = Search.dish_search(search_terms)
    	names = ["Seafood Gumbo","Seafood Gumbo","Mexican Gumbo","Spicy Southern Gumbo","Craft 2 - Mexican Gumbo"]
    	dish_names = []
    	for dish in dishes:
    		dish_names+= dish.name
    	self.assertEqual(names.sort(),dish_names.sort())





if __name__ == '__main__':
    unittest.main()