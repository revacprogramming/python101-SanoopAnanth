l=[]
while True:
  n=input('enter the number: ')
  if n == 'done':
    break
  try:
    flt=float(n)
  except:
    print('invalid input')
    continue
  l.append(flt)

l.sort()
a=len(l)
print('maximum =',l[a-1])
print('minimum =',l[0])

    
  
  