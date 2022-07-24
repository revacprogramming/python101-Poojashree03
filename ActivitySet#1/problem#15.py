Program 15
# make this code work 
 def input_set(): 
   s1=(input('Enter Set? ')).split(' ') 
   return s1 
 def get_operation(): 
   choice=input('Enter the operation to be performed (n/u)\nor to quit hit enter:') 
   return choice 
 def get_operands(): 
   choice=(input('Enter the operands (set1/set2/set3):')).split(' ') 
   l1 = list() 
   for operand in choice:  
         if operand == 'set1': 
             l1.append(set1) 
         elif operand == 'set2': 
             l1.append(set2) 
         elif operand == 'set3': 
             l1.append(set3) 
   
   return l1 
 def unionn(s1,s2): 
   s3 = s1 
   for ele in s2: 
       if ele not in s3: 
         s3.append(ele) 
   s3.sort() 
   return s3 
 def interr(s1,s2): 
   s3 = [] 
   for ele in s1: 
       if ele in s2: 
         s3.append(ele) 
   s3.sort() 
   return s3 
  
 def perform_operation(operation,operands): 
   r=[] 
   if 'u'==operation: 
     if len(operands)==2: 
       r=unionn(operands[0],operands[1]) 
     else: 
       rr=unionn(operands[0],operands[1]) 
       r=unionn(rr,operands[2]) 
   elif 'n'==operation: 
     if len(operands)==2: 
       r=interr(operands[0],operands[1]) 
     else: 
       rr=interr(operands[0],operands[1]) 
       r=interr(rr,operands[2]) 
   return set(r) 
        
 def main(): 
     global setu,set1,set2,set3 
     setu = input_set() 
     set1 = input_set() 
     set2 = input_set() 
     set3 = input_set() 
     while True: 
       operation = get_operation() 
       if operation=='': 
         break 
       operands = get_operands() 
       result = perform_operation(operation,operands) 
       print(result) 
     #print_report(setu,set1,set2,set3) # members in only s1 and s2, members in only s2,s3, members in only s3,s1, members not in s1,s2,s3 and members in all s1,s2,s3   
  
 main()