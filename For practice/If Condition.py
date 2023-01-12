a = int(input("Enter the Value")) # agar condition True h to output
if a%4 ==0:
    print(a,"Even Number")
else:
    print(a,"Odd Number")

per=int(input("Enter the Value:- "))
if per>= 60:
    print("First Division")
elif per>= 48: # We use 2time elif beacuse there are 4 time
    print("Second Division")
elif per>= 35:
    print("Third Divison")
else:
    print("Fail")

print('''
+ add
- subtract
* Multiplcation
/ duvide
''')
#num1 = int(input("Enter the value: 1"))
#num2 = int(input("Enter the value: 2"))
#opr = input("Enter the oper.. (+,-,*,/):-")
#if opr == "+":
    #print("num1+num2")
#if opr == "-":
    #print("num1-num2")
#if opr == "*":
    #print("num1*num2")
#if opr == "/":
    #print("num1/num2")
#else:
    #print(End)

for n in range(4):
    print(n)
print()
for n in range(1,5):
    print(n)
for n in range(2,21):
    print("2*",n,"=",2*n)
# in range reverse case:
for n in range(15,5,-1): # (15=length, 5=Upto, -1=Decrement)
    print(n)
#while loop (Start, Condition,Increment/Decrement)

p=1 # Kab tak chalana h (Start)
while p<=8: # Condition
    print("Bhanu")
    p = p+1 # Increment
a=7
while a>=1:
    print("I am here")
    a=a-1

