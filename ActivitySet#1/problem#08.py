fname=input('enter file name: ')
fh=open(fname)
total=0
count=0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        pos=line.find(':')
        flt=float(line[pos+1:])
        total+=flt
        count+=1
print('average spam confidence: ',total/count)
