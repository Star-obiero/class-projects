num=10
num2=0

try:
    print(num/num2)#try this code ,if it fails
except:
    print("you can not divide by zero")#run this block instead

#Trying user input safely
try:
    age=int(input("Enter your age:"))
    print("your age is",age)
except:
    print("Please enter a valid age")

#Catching specific extraction

try:
    result=10/0
    print(result)
except ZeroDivisionError:
    print("Error:You canot devide by zero9")

#Handling multiple exception

try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter secont number:"))
    print("Result=",num1/num2)
except ValueError:
    print("Please enter number only")
except ZeroDivisionError:
    print("second number can not be zero7")

#One except for multiple errors

try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter the second number:"))
    print("Result=",num1/num2)
except(ValueError,ZeroDivisionError):
    print("Invalid or devision by zero")

#Using else-runs only if there is no exception

try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter the second number:"))
    result=num1/num2
    print("Result=",result)
except(ValueError,ZeroDivisionError):
    print("Invalid or devision by zero")

else:
    print("Division successful")
    print("Result",result)

#using finally-always run

try:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter the second number:"))
    result=num1/num2
    print("Result=",result)
except(ValueError,ZeroDivisionError):
    print("Invalid or devision by zero")
else:
    print("The answer is ",result)
finally:
    print("Execution complete")