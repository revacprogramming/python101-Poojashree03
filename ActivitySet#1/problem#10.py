Program 10
# Dictionaries 
 name = input("Enter file:") 
 if len(name) < 1: 
     name = "mbox-short.txt" 
 handle = open(name) 
 d={} 
 for line in handle: 
     if line.startswith('From:'):continue 
     if not line.startswith('From'):continue 
     st=line.split() 
     word=st[1] 
     d[word]=d.get(word,0)+1 
      
 l=0 
 s='' 
 for a,b in d.items(): 
     if b>l: 
         l=b 
         s=a 
 print(s,l)

