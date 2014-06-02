from Venue import Venue

v = Venue('5152ec38d9b848b767e8', 'venue')
print v.categories
not_rest = lambda venue: all(c in ['restaurant', 'other'] for c in venue.categories )
print not_rest(v)


