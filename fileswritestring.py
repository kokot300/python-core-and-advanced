import os
import sys

if os.path.isfile("trainingfile.txt"):
    print("write something (when finished, type #):\n")
    x=''
    while x!='#':
        x=input()
        print(x)
        f=open("trainingfile.txt","a")
        print("opened")
        f.write(x)
        f.write("\n")
    print("written")
    f.close()
    f=open("trainingfile.txt","r")
    r=f.read()
    print(r)
    f.close()
    print("closed")
else:
    print("file not found!")
    sys.exit(0)