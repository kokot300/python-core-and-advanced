from functools import reduce

lst=[5,10,15,20]

r=reduce(lambda x,y:x+y,lst)

print(r)