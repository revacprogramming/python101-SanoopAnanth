# Conditional Execution
hrs=float(input("enter the hrs "))
pay=float(input("enter the pay "))
if(hrs>40):
  overtime=(hrs-40)*(pay*0.5)
  tp=(hrs*pay)+overtime
else:
  tp=hrs*pay
print("total pay=",tp)
  
