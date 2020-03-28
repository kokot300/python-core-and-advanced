import encapsuleh as aaa

c=aaa.Student()
c.disp()
print(c._Student__id) #however you can access it this way

print("\n")

s=aaa.Studenten()
s.setId(123)
s.setName("john")
print(s.getId())
s.disp()