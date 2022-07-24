Program 3
n=int(input()) 
 for i in range(n): 
   l=int(input()) 
   st=input() 
   for j in range(l): 
     for k in reversed(range(l+1)): 
       if k-j<3: 
          break 
       ss=st[j:k] 
       if ss==ss[::-1]: 
           print(ss,j+1)