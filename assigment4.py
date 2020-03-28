x=int(input("enter a number\n"))
i=0
while i<x:
    i+=1
    if i%10==0:
        continue
    elif i>100:
        break
    else:
        print(i)

"""
x=int(input("enter a number\n"))
for i in range(1,x+1):
    if(i%10==0):
        continue
    elif(i>100):
        break
    else:
        print(i)
"""