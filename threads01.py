#t=Thread(target=functionName,args)
#t.start()
#class MyThread(thread)
#   display()
#   t=Thread(target=myobj.display,args)
#   t.start()
#override the ride

import threading

print(threading.currentThread().getName())

if threading.currentThread()==threading.main_thread():
    print("main")
else:
    print("not main")

def displaynumbers():
    for i in range(0,11):
        print(i)
        print(threading.currentThread().getName())

t=threading.Thread(target=displaynumbers)
t.start()