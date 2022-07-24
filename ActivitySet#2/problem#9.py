Program 9
class Menu(dict): 
   """fill in class definition here""" 
   def __init__(self): 
     self.d={} 
   def __setitem__(self,key='',value=0): 
     if(key in self.d): 
         self.d[key]+=value 
     else: 
         self.d[key]=value 
   def __str__(self): 
     return 'Menu:\n'+('\n'.join([str(a+' '+str(b)) for a,b in self.d.items()])) 
      
 class Order: 
   def __init__(self,Menu): 
     self.d1={} 
     self.class_m=Menu.d 
   def __setitem__(self,key1='',value1=0): 
     if key1 in self.class_m: 
         if self.class_m[key1]>=value1: 
           self.d1[key1]=value1 
         else: 
           self.d1[key1]=self.class_m[key1] 
           print('Not enough quantity but can provide',self.class_m[key1]) 
     else: 
       raise KeyError("Item not in menu") 
            
   def __str__(self): 
     return 'Your Order:\n'+('\n'.join([str(a+' '+str(b)) for a,b in self.d1.items()])) 
        
 class Bill: 
   def __init__(self,Menu,Order): 
     self.m=Menu.d 
     self.o=Order.d1 
   def __str__(self): 
     st='Bill:\n' 
     st+=('\n'.join([str(a+' '+'Rs.'+str(b*20)) for a,b in self.o.items()])) 
     total=0 
     for v in self.o.values(): 
       total+=(v*20) 
     st+='\nThe total Amount:\n'+'Rs.'+str(total) 
     return st 
      
 m = Menu() 
 m["idly"] = 20 
 m["vada"] = 20 
 print(m) 
 o = Order(m) 
 try: 
     o["vada"] = 4 
     o["idly"] = 4 
     o["pongal"] = 2 
  
 except KeyError as e: 
     print(e) 
  
 print(o) 
 b = Bill(m, o) 
 print(b)