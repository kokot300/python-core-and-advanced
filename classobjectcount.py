class objCounter:
    numObj=0

    def __init__(self):
        objCounter.numObj+=1 #if self.numObj then line 15 returns 0

    @staticmethod
    def dipsl(): #this method is static
        print(objCounter.numObj)


o1=objCounter()
o2=objCounter()

objCounter.dipsl()