try:
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    operation=input("Enter operator(+,-,/,*):")

    if operation=="+":
        print("Result=",num1+num2)

    elif operation=="-":
        print("Result=",num1-num2)
    elif operation=="*":
        print("Result=",num1*num2)
    elif operation=="/":
        print("Result=",num1/num2)
    else:
        print("Invalid operator")
except(ValueError,ZeroDivisionError):
    print("Value error or division by zero")
finally:
    print("Calculator closed")