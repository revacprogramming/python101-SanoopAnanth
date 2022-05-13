# Loops & Iterators
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    print(num)
    try:
      flsv=float(num)
    except:
      print('Invalid input')
      continue
    for i in num:
       if smallest is None:
            smallest=num
       elif num<smallest:
            smallest=num
    for i in num:
        if largest is None:
            largest=num
        elif num>largest:
            largest=num
  
      
print("Minimum",smallest)
print("Maximum", largest)

      
      
    