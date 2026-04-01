"""#Raing your own exception
age=-5
if age <=0:
    raise ValueError("Age can not be less than zero")
"""
#Practical use of "raise"

balance=500
amount=int(input("Enter amount to withdraw"))

if amount > balance:
    raise ValueError("Insufficient balance")

print ("withdrawl successful")

#Assertion that pass
num = 5
assert num > 0,"Number must be posituve"
print ("Valid number")

#Exception agument
try:
    x=10/0
except ZeroDivisionError as e:
    print("Error message:",e)