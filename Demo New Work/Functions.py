
def greet():
    print("Hello")
    print("Good Morning")
greet()

def add_sub(x,y):
    c = x+y
    d = x-y
    return c,d

result1,result2 = add_sub(8,7)
print(result1, result2)