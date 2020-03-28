class Student:
    majar="CSE" #this one is static and is equal to all objects

    def __init__(self,rollno,name):
        self.rollono=rollno
        self.id=name

    def displ(self):
        print(self.rollono)
        print(self.id)
        print(self.majar)
        print("\n")

s1=Student(1,"john")
s2=Student(2,"Mark")

s1.displ()
s2.displ()