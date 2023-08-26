try:
    a=int(input("Enter number1:"))
    b=int(input("Enter number2:"))
    print("Sum:",a+b)
except Exception as e:
    #print("Error!")
    print(e)
else:
    print("This is finally block!")
    print("Mul:",a*b)