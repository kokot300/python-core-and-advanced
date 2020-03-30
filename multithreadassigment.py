#!/bin/usr/python
from threading import *
from time import sleep

class NumPrint:
    def __init__(self,start,stop):
        self.start=start
        self.stop=stop
        self.c=Condition()
    def Printer(self):
        self.c.acquire()
        #self.c.wait(timeout=0.1)
        for i in range(self.start,self.stop,2):
            self.c.acquire()
            self.c.wait(timeout=1)
            print(i,"\n")
            sleep(0)
            self.c.notify()
            self.c.release()

class Coordinator:
    def __init__(self,t1,t2):
        #self.odd=t1.start()
        #self.even=t2.start()
        self.alll=[]
        self.c=Condition()

    def warkocz(self):
        self.c.acquire()
        print(t1.start())
        self.c.wait(timeout=0)
        print(t2.start())
        #even.start()
        #odd.start()
        #self.alll.append(self.odd)
        #self.alll.append(self.even)
        #print(self.alll)

oodd=NumPrint(1,101)
eeven=NumPrint(2,101)
t1=Thread(target=oodd.Printer)
t2=Thread(target=eeven.Printer)
coor=Coordinator(t1,t2)
#coor=Coordinator(t1.start(),t2.start())
t3=Thread(target=coor.warkocz)
t3.start()

