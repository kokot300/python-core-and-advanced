class Programer:
    def setName(self,n): #setter methid
        self.name=n
    def getName(self): #getter method
        return self.name

    def setSalary(self,s):
        self.salary=s
    def getSalary(self):
        return self.salary

    def setTech(self,t):
        self.technologies=t
    def getTech(self):
        return self.technologies

p1=Programer()
p1.setName("john")
p1.setSalary(100)
p1.setTech("java")

print(p1.getName())
print(p1.getSalary())
print(p1.getTech())