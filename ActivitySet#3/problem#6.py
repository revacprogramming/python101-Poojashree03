Program 6
r={} 
 for i in range(int(input())): 
   points=int(input()) 
   if points<=0: 
     r['0']=1 
     continue 
   f1,f2,s=0,0,0 
   f3=1 
   for j in range(points): 
     s=f1+f2+f3 
     f1=f2 
     f2=f3 
     f3=s 
   r[str(points)]=s 
 for a,b in r.items(): 
   print(f'{a} points: {b} ways')