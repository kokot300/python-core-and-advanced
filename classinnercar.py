class Car:
    def __init__(self,make,year):
        self.mark=make
        self.age=year

    class Engine:
        def __init__(self,numm):
            self.number=numm

        def start(self):
            print("engine started")

c=Car("bmw",1994)
e=c.Engine(123)
e.start()