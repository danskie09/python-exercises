a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]



num = int(input("input a number:   "))


filtered = [i for i in a if i < num]

newList = list(set(filtered))

print(newList)





