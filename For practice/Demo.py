t=['Bhanu','Sharma','Prakash'] # For List
print(t)
t[1]='16'
print(t)

t= ('Bhanu','Sharma','Prakash')
print(t)
#t[3]="Sharma"
#print(t)

d = {'Course name': 'Python', # For Dictonary
     'Duration': '2month'}
print(d)
print(d['Course name'])

s={'Bhanu','Munish','Munish'}
print(s)

#Input from User
a=input("Enter the value 1:-")
b=input("Input the value 2:-")
print(a+b) #Now they combine value like they not add just combine

a=int(input("Enter the value 1:-")) # Take int no convert flot use flot
b=int(input("Enter the value 2:-"))
print(a+b) # Now its convert str into int

a= eval(input("Enter the value 1:-")) # Eval take any value ex-20.5,45 etc
b= eval(input("Enter the value 2:-"))
print(a+b) # Now its convert str into int
