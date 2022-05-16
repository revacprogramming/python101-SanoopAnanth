# Lists

#filename = "dataset/romeo.txt"
file=input('enter file name: ')
fh=open(file)
t=[]
for line in fh:
    str1=line.rstrip().split()
    for ele in str1:
        if ele not in t:
            t.append(ele)
        else:
            continue
t.sort()
print(t)
