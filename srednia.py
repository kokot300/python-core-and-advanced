c=12

def average(a,b):
    c=(a+b)/2
    d=a-b
    print(globals()['c'])
    return c,d

aaa=average(1,2)

for i in aaa:print(i)

bbb=average
bbb(1,4)