from array import *
arr = array('i',[])
n = int(input("Enter the input of the array"))
for i in range(n):
    x = int(input("Enter the next value"))
    arr.append(x)
print(arr)
k = 0
vals = int(input("Enter the value for search"))
for e in arr:
    if e== vals:
        print(k) #Manual array
        break
    k+=1
print(arr.index(vals)) # array with function

from numpy import