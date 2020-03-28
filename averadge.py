lst=[int(x) for x in input("enter 3 numbers \n").split()]
print(lst)

s=lst[0]+lst[1]+lst[2]
d=s/len(lst)
print("average is %f\n"%(d))