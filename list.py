lst=[1,2,3,30.5,-1,'kokot']
print(lst)
print(lst[1])
print(lst[-1])
print(lst[1:3])
print(lst[0:4:2]) #step
print(len(lst))
print(lst*2)

lst.append(122)
print(lst)
lst.remove(122)
print(lst)
del(lst[1])
print(lst)
lst.clear()
print(lst)

lst=[1,2,3,30.5,-1,'kokot']
lst.remove('kokot')
print(max(lst))
print(min(lst))
lst.insert(2,33) #inserts in 2nd index value 33
print(lst)
lst.sort() #print(lst.sort()) doesn't work :(
print(lst)
lst.sort(reverse=True)
print(lst)