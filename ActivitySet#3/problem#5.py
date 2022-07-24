Program 5
import numpy as np 
 def valid_row(arr): 
   for k in range(9): 
     #checking wheather it is in range of 0-9 
     if arr[k] not in range(0,10): 
       return -1 
     else: #checking for repeated values 
       if arr[k]!=0: 
         if arr[k] in arr[k+1:10]: 
           return -1 
            
 def valid_col(arr,i): 
   l=[] 
   for k in range(9): 
     #checking wheather it is in range of 0-9 
     if arr[k][i] not in range(0,10): 
       return -1 
     else: #checking for repeated values 
       if arr[k][i]!=0: 
         l.append(arr[k][i]) 
   if len(l) != len(set(l)): 
     return -1 
            
 def valid_sub_matrix(arr): 
   sub_l='' 
   h=1 
   for i in range(0,9,3): 
     for j in range(0,9,3): 
       l=[] 
       for si in range(i,i+3): 
         for sj in range(j,j+3): 
           if arr[si][sj]!=0: 
             l.append(arr[si][sj]) 
       if len(l) != len(set(l)): 
         sub_l+=str(h) 
       h+=1 
   return sub_l 
  
 def main(): 
   n, m = 9,9 
   d={'rows:':'','columns:':'','sub-matrix:':''} 
   no = int(input()) 
   for i in range(no): 
     arr = np.array([input().strip().split() for _ in range(n)], int) 
     for j in range(9): 
       r1=valid_row(arr[j]) 
       if r1==-1: 
         d['rows:']+=str(j+1) 
       r2=valid_col(arr,j) 
       if r2==-1: 
         d['columns:']+=str(j+1) 
     d['sub-matrix:']=valid_sub_matrix(arr) 
     if d['rows:']==d['columns:']==d['sub-matrix:'] == '' and 0 in arr: 
       print('incomplete but viable') 
     elif d['rows:']==d['columns:']==d['sub-matrix:'] == '': 
       print('complete') 
     else: 
       print(f"Non-Viable\nrows:{d['rows:']}\ncolumns:{d['columns:']}\nsub-matrix:{d['sub-matrix:']}") 
  
 main()