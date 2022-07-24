Program 2
def add(a, b): 
     return a+b 
  
 def output(a, b, sum): 
     print(f'{a}+{b} is {sum}') 
  
 def input_two_numbers(): 
     n1,n2=input('input?').split() 
     return int(n1),int(n2) 
    
 def main(): 
     a, b = input_two_numbers() 
     sum = add(a, b) 
  
     output(a, b, sum) 
  
  
 if __name__ == '__main__': 
     main()