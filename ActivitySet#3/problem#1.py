Program 1
def rarea(f): 
   a=f[0]*(f[3]-f[5]) 
   b=f[2]*(f[5]-f[1]) 
   c=f[4]*(f[1]-f[3]) 
   return(abs(a+b+c)) 
  
  
 def outpp(ch,resl): 
     j=0 
     for i in ch: 
         print(f'Area of rectangle with vertices ({ch[j][0]},{ch[j][1]}),({ch[j][2]},{ch[j][3]}),({ch[j][4]},{ch[j][5]}) is {resl[j]}') 
         j+=1 
      
  
 ll,ch=[],[] 
 for i in range(int(input())): 
   rl=list(map(float,input().split())) 
   ch.append(rl) 
   ll.append(rarea(rl)) 
    
 outpp(ch,ll)