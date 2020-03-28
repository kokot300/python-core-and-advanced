while True:
    f=open("file1","w")
    lst=[x for x in input("enter 2 numbers:\n").split(sep=None,maxsplit=1)]
    print("you entered: ",lst)
    f.write("you entered: %s \n" %lst[0])
    f.write("you entered: %s \n" % lst[1])
    try:
        d=int(lst[0])/int(lst[1])
        print("division returns: ", d)
        f.write("division returns: %f \n" %d)
    except ZeroDivisionError:
        print("can't divide by zero!")
        f.write("can't divide by zero!")
    else: #only if try successfull
        print(("all right!"))
        break
    finally: #try successfull or not
        f.close()
        print("file closed!")