class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s1=Student("Prince",20) 
s2=Student("Alice",18)

print(s1.name)
print(s2.age)



class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed

d1=Dog("Bingo","German Shepherd")
d2=Dog("max","Bull dog")

print(d1.name,"-",d1.breed)
print(d2.name,"-",d2.breed)

# Methods

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
s1=Student("Prince",20)

s1.display()


#Class varieable

class Employee:
    "This class represents an employee and keeps track of the total number of employees created."
    empcount=0 #class variable
    def __init__(self,name):
        self.name=name
        Employee.empcount+=1

e1=Employee("Alice")
e2=Employee("Bob")
e3=Employee("Charlie")
print("Total employee:",Employee.empcount)

#Class verieable vs instance variable

class car:
    wheels=4
    def __init__(self,brand):
        self.brand=brand

c1=car("Toyota")
c2=car("BMW")

print(c1.brand)
print(c2.brand)

print(car.wheels)

#Accessing attribute

class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
b1=Book("The Great Gatsby","F. Scott Fitzgerald")
print(b1.title)
print(b1.author)

b1.title="Investments"
print("After:"  ,b1.title)

#Adding new atribute dynamically
s1.course="Computer Science"
print(s1.course)

#Deleting attribute
#del s1.age
#print(s1.age) #This will raise an error because age attribute is deleted


#Built-in attributes
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__dict__)
print(Employee.__bases__)

#Destractor

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        print("Point object is being destroyed")

p1=Point(2,3)
del p1


class Person:
    def __init__(self,name):
        self.name=name

    def greet(self):
            print("Hello,",self.name)

class Patient(Person):
        def study(self):
            print(self.name,"is studying")

s1=Patient("Prince")   
s1.greet()
s1.study()

class BankAccount:
    bank_name="KCB_bank"
    def __init__(self,bank_name,balance):
        self.bank_name=bank_name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposit successful. New balance:",self.balance)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdrawal successful. New balance:",self.balance)
        else:
            print("Insufficient funds. Current balance:",self.balance)
    def display_balance(self):
        print("Current balance:",self.balance)
        print("Bank name:",self.bank_name)