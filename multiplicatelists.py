r=[]
lst0=[1,2,3,4,5,6,7,8,9,10]
lst1=[1,2,3,4,5,6,7,8,9,10]

r=[lst0[i]*lst1[i] for i in range(len(lst0))]

print(r)