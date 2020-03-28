#!bin/usr/python
from threading import *

class BookMyBus:
    def __init__(self,seats):
        self.seats=seats
        self.l=Lock()

    def buy(self,seatsRequested):
        self.l.acquire()
        print("seats available ", self.seats)
        print("you asked for ", seatsRequested)
        if self.seats>=seatsRequested:
            print("confirming seat")
            print("processing payment")
            print("printing ticket")
            self.seats-=seatsRequested
        else:
            print("no tickets left")
        self.l.release()

object=BookMyBus(10) #10 tickets available
t0=Thread(target=object.buy,args=(3,))
t0.start()
t1=Thread(target=object.buy,args=(4,))
t1.start()
t2=Thread(target=object.buy,args=(5,))
t2.start()