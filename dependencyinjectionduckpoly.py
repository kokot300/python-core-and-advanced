class Flight:
    def __init__(self,engine):
        self.engine=engine

    def startEngine(self):
        self.engine.startt()

class AirbusEngine:
    def startt(self):
        print("starting airbus")

class BoeingEngine:
    def startt(self):
        print("starting boeing")

ae=AirbusEngine()
f=Flight(ae)
f.startEngine()

be=BoeingEngine()
ff=Flight(be)
ff.startEngine()