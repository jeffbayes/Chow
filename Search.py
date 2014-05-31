from locu import MenuItemApiClient
from locu import VenueApiClient

class Search:
	def __init__(self):
		pass

	@staticmethod
	def search_venues(name,locality='',region=''):
		"""
		Uses the locu api to search for a venue by name.
		The default locality and region is '' which is searching everywhere.
		Also filters out venues that are not classified as 'other' or 'restraunt'

		args:
		name: string name of venue

		"""
		venues = []
		results = venue_client.Search(locality=locality,region=region,name=name)
		if results["objects"]:
			for locu_objects in results["objects"]:




		return None





	

