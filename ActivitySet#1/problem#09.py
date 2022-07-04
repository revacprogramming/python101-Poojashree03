#Lists

#filename = "dataset/romeo.txt"
filename = "dataset/romeo.txt"
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    if line == " " : continue
    words = line.split()
    for i in words:
        if i in lst:
            continue
        else:
            lst.append(i)
lst.sort()
print(lst)