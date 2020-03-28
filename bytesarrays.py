lst=[20,30,255]
print(lst)
print(type(lst),"\n")

#can't modify
b=bytes(lst) #bytes supports numbers up to 256 otherwise returns error
print(b)
print(type(b))
print(b[1],"\n")
#b[3]=22 #can't do that

b1=bytearray(lst)
print(b1)
print(type(b1))
print(b1[2])
b1[2]=22
print(b1[2])