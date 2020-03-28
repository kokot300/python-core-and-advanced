from abc import abstractmethod

class BMW:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def stopeng(self): #this function is inherited
        print("stopping engine")

    @abstractmethod
    def drive(self): #is abstract because there is no implementation, we only obligue children to use it
        pass

class ThreeSeries(BMW):
    def __init__(self,control,make,model,year):
        #BMW.__init__(self,make,model,year)
        super().__init__(make,model,year) #cleaner than above
        self.controlcruise=control

    def stopeng(self):
        super().stopeng()
        print("stopping")

    def drive(self):
        print("driving")

class FiveSeries(ThreeSeries):
    def __init__(self,parking,control,make,model,year):
        ThreeSeries.__init__(self,control,make,model,year)
        self.park=parking
    def stopeng(self):
        print("five series stopping") #overwriten
    def drive(self):
        print("driving")

three=ThreeSeries(True,"tdi",306,1991)
five=FiveSeries(False,False,"yo",3000,1992)
print(three.controlcruise)
print(five.model)
three.stopeng()
five.stopeng()
five.drive()
#FiveSeries.stopeng() #returns error
abb=BMW("tdi",306,1991) #no error
print(abb.year)
abb.drive()
