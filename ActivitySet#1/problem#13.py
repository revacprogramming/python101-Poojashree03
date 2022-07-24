Program 13 
# Network Programming 
 # https://www.py4e.com/lessons/network 
 import urllib.request, urllib.parse, urllib.error 
 from bs4 import BeautifulSoup 
 import ssl 
  
 # Ignore SSL certificate errors 
 ctx = ssl.create_default_context() 
 ctx.check_hostname = False 
 ctx.verify_mode = ssl.CERT_NONE 
  
 url = input('Enter URL - ') 
 c = int(input('Enter count:')) 
 p = int(input('Enter position:')) 
  
 for i in range(c): 
     html = urllib.request.urlopen(url, context=ctx).read() 
     soup = BeautifulSoup(html, 'html.parser') 
     gh=1 
     # Retrieve all of the anchor tags 
     tags = soup('a') 
     for tag in tags: 
         if(gh==p): 
            url=tag.get('href', None) 
         gh+=1 
     print('Retrieving:',url) 
       