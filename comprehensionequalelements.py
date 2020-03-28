r=[]
lst0=[1,2,4,6]
lst1=[1,3,5,6,7]

"""
for i in range(len(lst0)):
    for ii in range(len(lst1)):
        if lst0[i]==lst1[ii]:
            r.append(lst0[i])
        else:
            continue
"""

"""
for i in lst0:
    if i in lst1:
        r.append(i)
"""

r=[i for i in lst0 if i in lst1]

print(r)