from locu import MenuItemApiClient
from locu import VenueApiClient
import sys
import simplejson as json



global KEY
KEY = '2d36afa81b05f641ec3382d9992b8cec3d64a4e4'


s_type = sys.argv[1].strip()
if s_type =="v" or s_type == 'm':
	print  "in if"
	client = VenueApiClient(KEY)
elif s_type =="d":
	client = MenuItemApiClient(KEY)

raw_in= sys.argv[2].strip()
search_terms = raw_in.split(',')


resp = client.search(name =search_terms[0],locality=search_terms[1],region=search_terms[2])


if s_type == "v" or s_type =="d":
	print json.dumps(resp,indent=4, sort_keys=True)
else:
	dets = client.get_details(resp["objects"][0]["id"])
	print json.dumps(dets,indent=4, sort_keys=True)





