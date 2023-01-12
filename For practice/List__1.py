# list_1 = [12,45,78,45,12,95]
# list_2 = [45,78,26,45,78,45,12,33]
# for a,b in zip(list_1,list_2):
#     print(a,b)
# t=len(list_1) #length of list
# for a in range(t):
#     print(list_1[a],list_2[a])
# v=input("Enter the Name") #Convert into list
# print(v)
# l=v.split()
# print(l)
# l=[]
# for a in range(1,4):
#     n= input("Enter the value"+str(a)+":-")
#     l.append(n)
# print(l)

Data = {'Bharatpur':'321001', 'Jaipur':'302012'}
Data.values()
print(Data['Bharatpur'])
for i in Data.values():
    print(i)

d ={"Bhanu":'Python',"Munish": "Python","Bharatpur":'321001',"Jalander":"Selenium"}
d.values()
d.keys()
print(d["Bharatpur"])
print(d["Munish"])

