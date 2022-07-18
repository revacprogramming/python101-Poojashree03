# Using Web Services
# https://www.py4e.com/lessons/servces
import urllib.request, urllib.parse, urlllib.error
import xml.etreee.ElementTree as ET

url=input ('Enter url:')
print('Retrieving',url)

total=0
couunt=0

uh=urllib.request.urlopen(url)
data=uh.read()
print('Retrieveed',len(data),'characters')

tree=ET.fromstring(data)
lst=tree.findall('comments/comment')

for item in lst:
  count=count + 1
  t=item.find ('count').text
  total=total + float(t

 print('Count:', count)
 print('Sum:', total)                     
