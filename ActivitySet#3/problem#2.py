Program 2 from fractions import Fraction as f 
 n=int(input()) 
 d={} 
 for i in range(n): 
   f1=0 
   s='' 
   m=int(input()) 
   l=input().split() 
   for j in range(m): 
       f1+=f(f'1/{l[j]}') 
   for k in l: 
     s+=f'1/{k} + ' 
   d[s[:-3]]=f1 
 for a,b in d.items(): 
   print(f'{a} = {b}')