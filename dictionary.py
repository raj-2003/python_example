d={100:"Raj",200:"Manya",300:"Ronik",400:"Heli"}

print(d)
d1=d.copy()
print(d1)

print(d.get(100))
print([200])
print(d[200])
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(300))
print(d)


d2={500:"aayush",600:"aryan",700:"yash",800:"kush"}
d.update(d2)
print(d)
d[900]="deep"
print(d)

for i in d:
    print(i)

for i in d:
    print(i," : ",d[i])
