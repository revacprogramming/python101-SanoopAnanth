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
            smallest=flsv
       elif flsv<smallest:
            smallest=flsv
    for i in num:
        if largest is None:
            largest=flsv
        elif flsv>largest:
            largest=flsv
  
      
print("Minimum",smallest)
print("Maximum", largest)

      
      
    