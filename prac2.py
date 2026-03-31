
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
    def display(self):
        print("Current balance:",self.balance)
        print("Bank name:",self.bank_name)

acc=BankAccount("Prince",1000)
acc.display()
acc.withdraw(200)
acc.deposit(500)
acc.display()

print("Bank name:",BankAccount.bank_name)
print(acc)


class Robot:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    def introduce(self):
        print("Hello, I am",self.name,". I am",self.color,"and weigh",self.weight,"kg.")


r1=Robot("Robo1","red",50)
r1.introduce()
r2=Robot("Robo2","blue",60)
r2.introduce()

class Person(Robot):
    def __init__(self,name,personality,issitting,robotowned):
        self.name=name
        self.personality=personality
        self.issitting=issitting
        self.robotowned=robotowned
    def stand_up(self):
        issitting=False
    def sit_down(self):
        issitting=True
p1=Person("Prince","friendly",True,"Robo1")
p2=Person("Alice","curious",False,"Robo2")
print(p1.name,p1.personality,p1.issitting,p1.robotowned)