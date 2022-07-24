Program 9
# Lists 
 ll=[] 
 fname = input("Enter file name: ") 
 fh = open(fname) 
 for line in fh: 
     for tt in line.split(): 
         if tt not in ll: 
             ll.append(tt) 
  
 print(sorted(ll))