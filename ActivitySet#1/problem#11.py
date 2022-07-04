#Tuples

#filename = "dataset/mbox-short.txt"
# Tuples

#method 1

filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()


for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split(' ')
    words = words[6]
    #print(words.split(':'))
    hour = words.split(':')[0]
    counts[hour] = counts.get(hour, 0) + 1
for k,v in sorted(counts.items()):
     print(k,v)

  #method 2

filename = "dataset/mbox-short.txt"
name=input("Enter the file name:","r")
fhand=open(name)
fread=fhand.readlines()
d=dict()
for line in fread:
    if line.startswith("From "):
        l=line.strip()
        l=l.split()
       
        l=l[0:2]
        d[l]=d.get(l,0)+1
        term=sorted([(v,c) for v,c in d.items()])
for v,c in term:
    print(v,c)