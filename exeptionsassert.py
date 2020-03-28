try:
    num=int(input("enter even number:\n"))
    assert num%2==0, "even I said!" #program ends here :( if no try
except AssertionError as obj:
    print(obj)
print("and now we can continue")
