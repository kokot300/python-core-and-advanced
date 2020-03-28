class Student:
    def __init__(self):
        self.__id=1 #__ makes variable private
        self.__name="john"
    def disp(self):
        print(self.__name) #you can only access it inside class
        print(self.__id)

class Studenten: #that's tipical implementation of encapsulation
    def setId(self,idd):
        self.id=idd
    def getId(self):
        return self.id

    def setName(self,naam):
        self.name=naam
    def getName(self):
        return self.name

    def disp(self):
        print(self.getName())
        print(self.getId())