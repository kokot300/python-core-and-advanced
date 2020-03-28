dict1={1:"kokot",2:3,0:"krzysztof"}
print(dict1)
print(type(dict1))
print(dict1.items())
print(dict1.keys())
print(dict1.values())
print(dict1[1])
print("\n")

k=dict1.keys()
for i in k:print(i)
print("\n")

v=dict1.values()
for i in v:print(i)

print("\n")

del dict1[0]
print(dict1.values())
print("\n")

lst=["poland","germany","italy"]
lst.append("france")
lst.remove("france")
lst.insert(2,"france")

st={"poland","germany","italy"}
st.update(["france"])
st.remove("france")
