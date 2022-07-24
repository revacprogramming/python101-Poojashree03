Program 8
class Menu(dict): 
   def __setitem__(self,key='',value=0): 
     self.__dict__[key]=value 
   def __str__(self): 
     return ('\n'.join([str(a+' '+str(b)) for a,b in self.__dict__.items()])) 
   #represent a class's objects as a string 
   """ 
   def __repr__(self): 
       return repr(self.__dict__) 
   """ 
 m = Menu() 
 m["idly"] = 10 
 m["vada"] = 20 
 m["dosa"] = 50 
 print(m)