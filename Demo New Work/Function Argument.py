def update(x): #you can give any function name update, green etc
    print(id(x))
    x = 8
    print(x)

a = 10
update(a)
print(a)