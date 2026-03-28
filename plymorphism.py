class Lecture:
    lec_count=0
    def __init__(self,f,p,e):
        self.pfno=f
        self.phone=p
        self.email=e
        self.lec_count+=1
    def teach(self):
        print(self.email,"Teaching")


class Cod(Lecture):
    def __del__(self):
        print("deleating cod")
    def __init__(self,f,p,e,d):
        self.pfno=f
        self.phone=p
        self.email=e
        self.dept="computer science"
    def advise(self):






        
        print(self.email,"Advising students")

k=Cod(45,45654,"Geofrey","IT")
print()
k.advise()