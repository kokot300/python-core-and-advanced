i=True

while i==True:
    x=input("enter a number:\n")

    try:
        z=float(x)
        if z==0:
            print("you introduced 0\n")
            #i=False
            #return 0
        elif z%2==0:
            print("even\n")
        else:
            print("odd\n")
            #i = False
            #return 0
        i = False
    except ValueError:
        print("you haven´t introduced a number\n")
        i=True
