def decorfun(fun):
    def inner(n):
        r=fun(n)
        r+=" how are you?"
        print("n= ",n, type(n))
        print("fun(n)= ",fun(n))
        print("fun= ",fun)
        return r
    return inner

@decorfun
def hello(name):
    #print("hellofuntion",hello)
    return "hello "+name

print(hello("john"))