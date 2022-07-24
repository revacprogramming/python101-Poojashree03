Program 3
def get_cs(): 
     st=input() 
     return st 
    
 def cs_to_lot(cs): 
     j=[] 
     ll=cs.split(';') 
     for i in ll: 
        j.append(tuple(i.split('='))) 
     return j 
  
 def main(): 
     cs = get_cs() 
     lot=cs_to_lot(cs) 
     print(lot) 
  
  
 if __name__ == '__main__': 
     main()