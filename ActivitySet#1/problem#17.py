Program 17
#Networking 
 from urllib.request import urlopen 
 from bs4 import BeautifulSoup 
 import ssl 
  
 ctx = ssl.create_default_context() 
 ctx.check_hostname = False 
 ctx.verify_mode = ssl.CERT_NONE 
  
 url = input('Enter - ') 
 html = urlopen(url, context=ctx).read() 
 soup = BeautifulSoup(html, "html.parser") 
 suml=0 
 tags = soup('span') 
 for tag in tags: 
     suml+=int(tag.contents[0]) 
 print(suml)