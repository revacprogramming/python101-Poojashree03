Program 7
class Menu: 
   def __init__(self,name='',price=0): 
     self.my_menu=[] 
     self.my_menu.append((name,price)) 
   def __add__(self,a): 
     self.my_menu.append((a[0],a[1])) 
     return self 
   def __str__(self): 
     sd=self.my_menu[1:] 
     return ("\n".join([str(a+' '+str(b)) for a,b in sd])) 
    
  
 m = Menu() 
  
 m = m + ("idly", 10) + ("vada", 20) + ('dosa',50) 
  
 # Hint: operator overloading special methods (__add__, __sub__, etc.) 
 print(m)  # should print the menu properly 
 m1=Menu() 
 print(m1)