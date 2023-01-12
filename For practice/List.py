w = [1,2,3,4,5,6,7,8] #Get 5 nume
print(type(w))
print(w[5])
t = [1,2,3,[4,5,6,7]]
print(t[3][2])
r = [1,2,"Bhanu",[4,5,6,8]]
print(r[2]) # only Bhanu
print(r[0:3]) #Starting from 0 to Bhanu
print(r[2:]) #Starting from Bhanu to end
e=[1,2,3,4,5,6,7,8,9] # For argrument Skip 2
print(e[0::2])
r=[1,2,3,4,5,6,7,8,9] # reverse the list
print(r[-1::-1])

i=[10,20,30,40,50,60,70,80] # Getting the list by loop
u=len(i)
print(u)
for a in range(u): #with range
    print(i[a])
for a in i: #without range
    print(a)
for a in range(u-1,-1,-1):
    print(i[a])