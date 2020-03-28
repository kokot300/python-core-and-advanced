s="Hello World"
print (s)
print("lengh of ",s, " is ",len(s))
print(type(s),"\n")

s1="""hello
    world"""
print(s1)
print((s[1],s[5])*2) #not sure why
print(s[1:5]*2)
print(s[0:])
print(s[:8])
print(s[-1]) #goes from end
print(s.find("lo",0,len(s))) #returns cell where secuence starts; search in range (here whole string)
print(s.find("lo",0,2)) #returns -1 when not found
print(s.find("ss",0,len(s)))
print(s.count("o")) #there are 2 o's
print(s.replace("world","everybody"))
print(s.upper())
print(s.lower())
print(s.title())

#print(s[1,5]*2)
print(s[1:6:4]*2) #3rd value is step
print(s[10::-1]) #goes backwards
print(s[::-1])  #the same

print("\n")

s2=" love you "
print(s2.strip())
print(s2.lstrip())
print(s2.rstrip())
print(s2.strip("e")) #works directly in python here not :(