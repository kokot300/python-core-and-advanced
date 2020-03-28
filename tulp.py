#tuple is a list you can't modify

tlp=(1,2,3,50,"kokot",50)
print(tlp)
print(tlp[2])

t1=(1)
print(type(t1))

t2=(2,)
print(type(t2))

print(tlp.index(50))

lst=[1,20,45,"yo"]
print(type(lst))
t3=tuple(lst)
print(type(t3))
lst1=list(t3)
print(lst1)