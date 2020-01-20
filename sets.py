thisset={"apples", "bananas", "Oranges"}
print(thisset)
thisset.add("chai")
print(thisset)
for x in thisset:
    print(x)
thisset.remove("chai")

x={"a", "b", "c"}
y={"x", "c", "e"}
z={"w", "q", "r"}
result=x.intersection(y, z)
print(x)