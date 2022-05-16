# Lists

#filename = "dataset/romeo.txt"
file=input('enter file name: ')
fh=open(file)
t=[]
s=[]
for line in fh:
    str1=line.split()
    t.append(str1)
for ele in t:
    if(ele in s):
        continue
    else:
        s.append(ele)
        
print(s)