s={1,20,"kokot",20} #no indexing no slicing
print(s) #ignores repeated values!
print(type(s))
s.update([4])
print(s)
#print(s*3)
s.remove(20)
print(s)
f=frozenset(s) #can't update nor remove
print(f)
print(type(f))
#f.update([4]) #would give error