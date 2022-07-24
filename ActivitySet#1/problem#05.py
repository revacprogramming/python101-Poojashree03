Program 5
# Functions 
  
  
 def computepay(h, r): 
     if h<=40: 
         return h*r 
     else: 
         return ((40*r)+((h-40)*1.5*r)) 
  
 hrs = float(input("Enter Hours:")) 
 rt=float(input("Enter the rate:")) 
 p = computepay(hrs,rt) 
 print("Pay", p) 