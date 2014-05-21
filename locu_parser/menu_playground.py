from locu import MenuItemApiClient
from locu import VenueApiClient
try:
    import simplejson as json
except :
    import json

global KEY
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'

venue_client = VenueApiClient(KEY)
venue_id = '081653f66bf87bf8e205'
dets = venue_client.get_details('dc241e328c5cc445aea5')

for menu in dets["objects"][0]["menus"]:
	print "in the for loop"
	for section in menu["sections"]:
		for sub_section in section["subsections"]:
			for item in sub_section["contents"]:
				if item["type"] == "ITEM":
					print item.get("name","NA")
					print item.get("price","NA")


	