list1 = [1,2,3,4,5,7,78,4,5,89]
duplicates =[]
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]==list1[j]:
            duplicates.append(list1[i])
print(duplicates)
