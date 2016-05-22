#
##
### John Farrell
#### Search Instagram posts by locationID
##### Adapted from Gilad Lotan / Social Data Analysis

from urlparse import urlparse
from instagram.client import InstagramAPI
import pickle
import sys

# Fill in your API information
client_id = 'YOUR_ID'
client_secret = 'YOUR_SECRET'
api = InstagramAPI(client_id=client_id, client_secret=client_secret)


# Do your first location search
# See ReadMe for quick method to find Instagram location IDs
locationID=sys.argv[1]
iterations=sys.argv[2]

iterations = int(iterations)
locationID = int(locationID)
max_tag_id = ''
all_media = []
ans = api.location_recent_media(33,max_tag_id,locationID)

# Get your first media items and max_tag_id from that search
for m in ans[0]:
	all_media.append(m)
	parsed = urlparse(ans[1])
	params = {a:b for a,b in [x.split('=') for x in parsed.query.split('&')]}

# Iterate backwards through media, using max_tag_id, appending posts to the all_media array
# Increase the range() number to run more iterations for more data
for i in range(iterations):
	try:
	    max_tag_id = params['max_id']
	    ans = api.tag_recent_media(33,max_tag_id, locationID)
	    for m in ans[0]:
	        all_media.append(m)
	        
	    parsed = urlparse(ans[1])
	    params = {a:b for a,b in [x.split('=') for x in parsed.query.split('&')]}
	except AttributeError:
		break

# Save a pickle file to work off in the future
pickle.dump(all_media, open('%s_locationData.p'%locationID, 'wb'))