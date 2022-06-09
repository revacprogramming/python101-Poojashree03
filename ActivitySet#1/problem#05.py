# Functions


#def computepay(h, r):
    #pass  # ...


#hrs = float(input("Enter hours? "))
#rte = float(input("Enter rate per hour? "))

#p = computepay(hrs, rte)
#print("Pay", p)

def computepay(h,r): 
     if h > 40: 
         p = 1.5 * r * (h - 40) + (40 *r) 
     else: 
         p = h * r 
     return p 
      
 hrs = input("Enter Hours:") 
 hr = float(hrs) 
 rphrs = input("Enter rate per hour:") 
 rphr = float(rphrs) 
  
 p = computepay(hr,rphr) 
 print(p)
