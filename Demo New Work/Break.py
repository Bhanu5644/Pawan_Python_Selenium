
av = 5
x = int(input("how many candy you want"))

i = 1
while i <= x:
    if i > av:
        print("Out of Stock") #if Qty more than 5 its say out of stock
        break
    print("Candy")
    i = i+1
