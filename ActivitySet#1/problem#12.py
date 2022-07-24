Program 12
# Regular Expressions 
 # https://www.py4e.com/lessons/regex 
 import re 
 hand=input('Enter the file name:') 
 handle=open(hand) 
 total=0 
 for line in handle: 
      line=line.rstrip() 
      ss=re.findall('[0-9]+',line) 
      for i in ss: 
          total+=int(i) 
      
 print(total)
           
               
               

