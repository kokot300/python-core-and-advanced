#!/usr/bin/python
import logging

logging.basicConfig(filename="mylogdivision.log",level=logging.DEBUG)

while True:
    f=open("file","w")
    lst=[x for x in input("enter 2 numbers:\n").split(sep=None,maxsplit=1)]
    print("you entered: ",lst)
    f.write("you entered: %s \n" %lst[0])
    f.write("you entered: %s \n" % lst[1])
    try:
        d=int(lst[0])/int(lst[1])
        print("division returns: ", d)
        f.write("division returns: %f \n" %d)
        f.close()
        logging.info("division ok")
        break
    except TypeError:
        print("you haven't introduced right type of data!")
        f.write("you haven't introduced right type of data!")
        logging.error("something wrong")
    except ValueError:
        print("you haven't introduced correct values!")
        f.write("you haven't introduced correct values!")
        logging.error("something wrong")
    except ZeroDivisionError:
        print("can't divide by zero!")
        f.write("can't divide by zero!")
        logging.error("something wrong")
    except IndexError:
        print("enter TWO numbers!")
        f.write("enter TWO numbers!")
        logging.error("something wrong")
    # executes always no matter try True or False
    finally:
        f.close()
        print("file closed!")