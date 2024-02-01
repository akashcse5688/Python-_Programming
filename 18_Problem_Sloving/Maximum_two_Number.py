try:
    number1=int(input("Enter the first number ="))
    number2=int(input("Enter the second number"))
    if(number1>number2):
        print(f"{number1} is greater than number2")
    else:
        print(f"{number2} is grather than number1")
except:
    print("Invalid Input")