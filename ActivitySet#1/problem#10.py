#Dictionaries

#filename = "dataset/mbox-short.txt"
filename = "dataset/mbox-short.txt"
count=dict()
name = input("Enter the file name:")
handle = open(name,'r')
for line in handle:
    if not line.startswith('From '): 
        continue
    words=line.split()
    words=words[1]
    count[words]=count.get(words,0)+1
print(words, count[words])