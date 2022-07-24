Program 4
def get_cs(): 
     return(input()) 
    
 def cs_to_lot(cs): 
     j=[] 
     ll=cs.split(';') 
     for i in ll: 
        j.append(tuple(i.split('='))) 
     return j 
 def lot_to_cs(lot): 
     return (";".join([str(a+"="+b) for a,b in lot])) 
  
 def main(): 
     cs=get_cs() 
  
     lot=cs_to_lot(cs)  # convert connect string to list of tuples 
     print(lot) 
  
     cs=lot_to_cs(lot)  # convert list of strings to connect string 
     print(cs) 
  
  
 if __name__ == '__main__': 
     main()