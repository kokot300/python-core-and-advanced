#!/bin/usr/python
from threading import *
from time import sleep

class Prod:
    def __init__(self):
        self.products=[]
        #self.flag=False
        self.c=Condition()

    def produce(self):
        self.c.acquire()
        for i in range(1,5):
            self.products.append("Product"+str(i))
            sleep(1)
            print("added")
        #self.flag=True
        self.c.notify()
        self.c.release()

class Consumer:
    def __init__(self,prood):
        self.prod=prood

    def consume(self):
        self.prod.c.acquire()
        '''while self.prod.flag==False:
            sleep(0.2)
            print("waiting for orders")'''
        self.prod.c.wait(timeout=0)

        print("shipped"+str(self.prod.products))

p=Prod()
c=Consumer(p)

t1=Thread(target=p.produce)
t2=Thread(target=c.consume)

t1.start()
t2.start()