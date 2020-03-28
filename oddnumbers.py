while True:
    x=input("enter min number:\n")
    y=input("enter max number:\n")
    try:
        xx=int(x)
        try:
            yy=int(y)
            if xx%2!=0:
                while xx<=yy:
                    print(xx)
                    xx+=2
                #return 3
            else:
                xx+=1
                while xx <= yy:
                    print(xx)
                    xx+=2
                #return 4
        except ValueError:
            ValueError: ("you haven't introduced numbers")
            #return 2
    except ValueError:
        print("you haven't introduced numbers")