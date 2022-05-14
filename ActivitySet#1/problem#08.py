# Files

#filename = "dataset/mbox-short.txt"
fname=input('enter file name: ')
fopen=open(fname)
print(fopen)
count1=0
count2=0
for line in fopen:
  count1=count1+1
for line in fopen:
  if line=='X-DSPAM-Confidence:    0.8475':
    count2=count2+1
print('average spam confidence: ',count1/count2)