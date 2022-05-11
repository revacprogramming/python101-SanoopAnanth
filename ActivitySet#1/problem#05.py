# Functions


def computepay(h, r):
  if(h>40):
    overtime=(h-40)*(r*0.5)
    otp=(h*r)+overtime
  else:
    otp=h*r
  return otp
  
hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
