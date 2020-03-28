import threading
from time import sleep

class MyThread(threading.Thread):
    def run(self):
        threading.Thread.run(self)
        self.displaynumbers()

    def displaynumbers(self):
        sleep(5)
        for i in range(0, 11):
            print(i)
            print(threading.currentThread().getName())

class MyOwnThread:
    def displaynumbers(self):
        for i in range(0, 11):
            print(i)
            print(threading.currentThread().getName())

t=MyThread()
obj=MyOwnThread()
t2=threading.Thread(target=obj.displaynumbers)
t3=threading.Thread(target=obj.displaynumbers)

t.start()
t2.start()
t3.start()