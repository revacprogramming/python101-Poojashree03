Program 18
#database 
 import urllib.request, urllib.parse, urllib.error 
 import http 
 import sqlite3 
 import json 
 import time 
 import ssl 
 import sys 
  
 api_key = False 
 if api_key is False: 
   serviceirl = "http://py4e-data.dr-chuck.net/geojson?" 
 else: 
   serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json" 
  
   while True: 
     address = input('Enter location:') 
     if len(address)<1: break 
  
     url = serviceurl + urllib.parse.urlencode( 
        
       {'address':address}) 
     print('retriving',url) 
     uh = urllib.request.urlopen(url) 
     data = uh.read().decode() 
     print('retrived', len(data), 'characters') 
  
     try: 
       is = json.loads.(data) 
     except: 
       js = None 
  
     if hot js or 'status' not in js or js['status']!= 'OK': 
         print('failed to retrive') 
         print(data) 
         continue 
     print(json.dumps(js, indent=4)) 
     lat = js["results"][0]["geometry"]['location']["lat"] 
     lng = js["results"][0]["geometry"]['location']["lng"] 
     print('lat',lat,'lng',lng) 
     location = is['results'][0]['formated address'] 
     print(location)