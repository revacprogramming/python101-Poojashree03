Program 11 
name = input("Enter file:") 
 if len(name) < 1: 
     name = "mbox-short.txt" 
 handle = open(name) 
 d={} 
 t=() 
 for line in handle: 
     if line.startswith('From:'): continue 
     if not line.startswith('From'): continue 
     index=line.find(':') 
     s=line[index-2:index] 
     if s not in d: 
         d[s]=1 
     else: 
         d[s]+=1 
  
 t = tuple(d.items()) 
 result=sorted(t) 
  
 for a,b in result: 
     print(a,b)