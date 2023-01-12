m =[]
for a in range(1,101):
    m.append(a) #by append
print(m)
u=[y for y in range(1,21)] #list by list Comprehension Shortcut
print(u)
i="Hello"
d=[t for t in i]
print(d)

J= [20,80,4,50]
del J[2] #for select index
print(J)
J.pop(1) #Round Brackey for Pop
print(J)
e = [7,8,1,5,9]
e.remove(8) #for remove
print(e)
print(e.clear())
h=[45,87,65,78]
h[3]=85
print(h)
list_1 = [81,78,45,95,47]
list_1.insert(2,"Bhanu")
print(list_1)
print(list_1[2])
list_1.append(200)
print(list_1)
list_2=[1100,1500,7800]
g.extend(list_1)