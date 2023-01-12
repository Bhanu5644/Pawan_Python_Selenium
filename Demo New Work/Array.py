from array import *

vals = array('i',[5,9,8,4,8])
newArr = array(vals.typecode,(a*a for a in vals)) # for loop use
for i in newArr:
  print(i)