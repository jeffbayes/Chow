import unittest
from Search import Search

class SearchTest(unittest.TestCase):

    def test_venue_search(self):
        venues = Search.venue_search('belly',city='eugene',state='OR')
        names =[ "Belly","Taqueria Belly"]
        venue_names = [venue.name for venue in venues]
        self.assertEqual(names.sort(),venue_names.sort())




if __name__ == '__main__':
    unittest.main()