class Patient:
    def setId(self,idd):
        self.id=idd
    def setName(self,naam):
        self.name=naam
    def setSSN(self,ssnn):
        self.ssn=ssnn

    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getSSN(self):
        return self.ssn

    def disp(self):
        print(self.getId())
        print(self.getName())
        print(self.getSSN())

p=Patient()
p.setId(123)
p.setName("john")
p.setSSN(12345)
p.disp()