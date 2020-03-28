#!/bin/usr/python
from threading import *
from time import sleep

class Prod:
    def __init__(self):
        self.products=[]
        self.flag=False

    def produce(self):
        for i in range(1,5):
            self.products.append("Product"+str(i))
            sleep(1)
            print("added")
        self.flag=True

class Consumer:
    def __init__(self,prood):
        self.prod=prood

    def consume(self):
        while self.prod.flag==False:
            sleep(0.2)
            print("waiting for orders")

        print("shipped"+str(self.prod.products))

p=Prod()
c=Consumer(p)

t1=Thread(target=p.produce)
t2=Thread(target=c.consume)

t1.start()
t2.start()