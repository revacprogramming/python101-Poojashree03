Program 8 
# Files 
 fs=0.0 
 c=0.0 
 fname = input("Enter file name: ") 
 fh = open(fname) 
 for line in fh: 
     if not line.startswith("X-DSPAM-Confidence:"): 
         continue 
     st=line.find('0.') 
     fl=float(line[st:]) 
     fs+=fl 
     c+=1 
  
 print("Average spam confidence:",fs/c)