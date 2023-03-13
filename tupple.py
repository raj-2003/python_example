t=(1,2,2.2,"tops",[23,45,89],False)

print(t)
print(t.count(1))
print(t.index("tops"))
for i in t:
    print(i)
t[4].append(999)
print(t)
