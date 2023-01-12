# course = {'php':{"Duration":"2 Month","fees":"15000"},
#         'Java':{"Duration":"2 Month","fees":"10000"},
#         'Python':{"Duration":"2 Month","fees":"10000"}
#         }
# print(course)
# course['Java']["Duration"] ='3month'
# print(course['php']['fees'])
# for v,g in course.items():
#     print(v,g["fees"])



Family= {'Head':{'Papa':'59','Status':'Bussiness'},'Vice Head':{
        'Mummy':'45','Status':'Housewife'}, 'Wife':{'Vani':'29','Status':'Teacher'},
         'Husband':{'Bhanu':'31','Status':'Job'}
        }
Family['Head']['Papa']=63
print(Family)
for v,g in Family.items():
    print(v,g['Status'])
print(Family['Head']['Status'])
print(Family['Vice Head']['Status'])
print(Family['Wife']['Status'])
print(Family['Husband']['Status'])

# print(Family['Head']['Papa']['Status'])
# print(Family['Vice Head']['Mummy']['Status'])
# print(Family['Wife']['Vani']['Status'])
# print(Family['Husband']['Bhanu']['Status'])

# s ={10,20,30}
# s.pop()
# print(s)
# s.remove(20)
# print(s)
# s.add(80)
# print(s)

