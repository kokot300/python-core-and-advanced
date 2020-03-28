#!/usr/bin/python

while True:
    lst=[x for x in input("enter 2 numbers:\n").split(sep=None,maxsplit=1)]
    print("you entered: ",lst)
    try:
        d=int(lst[0])/int(lst[1])
        print(d)
        break
    except TypeError:
        print("you haven't introduced numbers!")
    except ValueError:
        print("you haven't introduced numbers!")
    except ZeroDivisionError:
        print("can't divide by zero!")