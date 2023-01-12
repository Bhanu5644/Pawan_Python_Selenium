b ="Welcome the world" # Index number what need to type
print(b[0:12])
print(b[0::2])
print(b[-1::-1]) # For name reverse

w = "Welocme hero"
l = len(w)
print(l)
for a in range(l):
    print(w[a])
print("")
for a in range(l-1,-1,-1):
    print(w[a])
print("")
w = "Welocme hero"
for a in w:
    print(a)

b= "Welcome Dear" # for Lower,Upper, Title,Capitalize case
a=b.lower()
print(a)
c=b.upper()
print(c)
d=b.title()
print(d)
e=b.capitalize()
print(e)

w="welcome" #Find index (Video 23)
print(w.find('e',2))
print(w.index("o"))
print(w.isalpha())
print(w.isdigit())
print(w.isalnum())

z = 75 # Chr commend
print(chr(z),z)

y= "A"
print(ord(y),y)

t="hello {} welcome to {} of tech".format("Wscube","World") # adding the Text middle in #Video 25
print(t)
y="hello {0} welcome to {1} of tech".format("Wscube","World") # adding the Text middle in
print(y)
w="hello {a:^14} welcome to {b} of tech".format(a="Wscube",b="World") # Spacing between character
print(w)
g="hello {a:<14} welcome to {b} of tech".format(a="Wscube",b="World") # Spacing between character
print(g)
i="hello {a:>14} welcome to {b} of tech".format(a="Wscube",b="World") # Spacing between character
print(i)