Program 22
'''02''' 
 from urllib.request import urlopen 
 import json 
 url='http://py4e-data.dr-chuck.net/comments_1550211.json' 
 jsFile = urlopen(url) 
 data =json.loads(jsFile.read()) 
 sum=0 
 for i in data['comments']: 
     sum+=i['count'] 
 print(sum)