Program4
# Conditional Execution 
  
 hrs =float(input("Enter Hours:")) 
 rt=float(input("Enter the rate:")) 
 if hrs<=40: 
     print(hrs*rt) 
 else: 
     h=hrs-40 
     print((40*rt)+(h*1.5*rt))