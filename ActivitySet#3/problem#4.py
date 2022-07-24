Program 4
def main(): 
   n = int(input()) 
   for i in range(n): 
     l=int(input()) 
     input_list= [int(x) for x in input().split()] 
     my_list=[] 
     j=0 
     while j<l: 
       if input_list[j]==0 and input_list[j+1]==0: 
         my_list.append(0) 
         j+=2 
       elif input_list[j]==0 and input_list[j+1]!=0: 
         for x in range(input_list[j+1]): 
             my_list.append(input_list[j+2]) 
         j+=3 
       else: 
         my_list.append(input_list[j]) 
         j+=1 
     for k in my_list: 
       print(k,end=' ') 
 main()