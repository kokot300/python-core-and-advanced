lst=[]
'''
for i in range(1,11):
    lst.append(i**3)
'''
lst=[x**3 for x in range(1,11) if x!=2]
print(lst)