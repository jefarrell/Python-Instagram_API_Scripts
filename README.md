Instagram-API-Data
=============================
Use python to query the Instagram API:  
- TagSearch returns all posts containing a given hashtag  
- LocationSearch returns all posts tagged with a given location ID
   

Both scripts by default request 33 media objects from Instagram.  The "numberofIterations" argument below specifies how many times to run through that loop.  For example, an argument of 5 will (potentially) return 165 objects (33/loop * 5 loops)
Both scrips save your query to a pickle file for later analysis
***


#### Tag Search  
Return all posts containing a given hashtag  
**Usage**:  
```python instagramTagSearch.py yourDesiredTag numberofIterations    
**Example**:
```python instagramTagSearch.py earthday 20
   
***
#### Location Search  
Return all posts tagged at given location ID  
**Usage**:  
```python instagramLocationSearch.py locationID numberofIterations      
**Example**:  
```python instagramLocationSearch.py 330936715 20  
   
**How to find a location ID**  
Easiest way is the [location search endpoint](https://www.instagram.com/developer/endpoints/locations/#get_locations_search)  
Start with a latitude/longitude point, and Instagram will return a list of location tags available near that point.  
```locationNames = api.location_search(lat=yourLatitude, lng=yourLongitude)  
```for m in locationNames:  
```print m  
```print m.name  
Use your desired location ID with the LocationSearch script  
   
   
   
   
Adapted from code by Gilad Lotan, from Social Data Analysis at NYU ITP
