a1 = 121212
a2 = 121212
print(id(a1))   #2064104623184
print(id(a2))   #2064104623184
a1 = 12
print(id(a1))   #1385412000
print(id(a2))   #2064104623184


li = [1, 2, 3, 4]
print(id(li))   #2646687915656
li.append(5)
print(id(li))   #2646687915656
va = li.pop()
print(va)       #5
print(id(li))   #2646687915656
li[0] = 11
print(id(li))   #2646687915656
li = [1, 2, 3, 4]
print(id(li))   #2988173663944
