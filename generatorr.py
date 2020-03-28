def customgen(x,y):
    while x<y:
        yield x
        x+=1

r=customgen(20,30)

for i in r:
    print(i)