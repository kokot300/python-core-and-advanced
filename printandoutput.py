import sys

print(1)
print("hello")
print("hello \n world \n\t hi")

a=10
b=20
print(a,b,sep=',') # instead of comma whatever

name="john"
marks=10

print("student's name is",name,"his mark is",marks)
print("student's name is %s his mark is %i"%(name, marks)) #%f for floating, %b for boolean...
print("student's name is {} his mark is {}".format(name,marks))

s=input("enter your name\n") #by default string
print(s)

ii=int(input("enter an integrer"))

lst=[x for x in input("enter 3 numers:\n").split()] #by default separates by space
print(lst)

lst=[int(x) for x in input("enter 3 numers:\n").split(",")]
print(lst)