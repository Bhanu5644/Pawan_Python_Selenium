list_1=[12,13,14,18,92]
list_1.insert(1,"Sharma")
print(list_1)
list_2=[45,78,19]
list_1.extend(list_2)
print(list_1)

######List Function#########
w=[10,78,45,12,45,95,63,12]
a=w.count(78) #count need to crete new variable
print(a)
e= max(w) # Max
print(e)
r= min(w) # Mininum
print(r)
g= sorted(w)
print(g)
w.reverse()
print(w)
d=w.index(45)
print(d)

u=[12,45,78,45,12,95] #Skip index same number
s=u.index(45,2)
print(s)
