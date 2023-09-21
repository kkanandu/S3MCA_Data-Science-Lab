import numpy as np
x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
      a=np.add(x,y)
      print("sum is",a)
    elif choice =='2':
      a=np.subtract(x,y)
      print("substration is",a)
    elif choice =='3':
      a=np.divide(x,y)
      print("division is",a)
    elif choice =='4':
      a=np.multiply(x,y)
      print("multiplication is",a)
    elif choice =='5':
      print("Exit")
      break
    else:
      print("invalid choice")





