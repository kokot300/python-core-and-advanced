x=int(input("enter a number:\n"))
flag=True

for i in range(2,x-1):
    if x%i==0:
        flag=False

if flag!=False:
    print("prime")
else:
    print("not prime")