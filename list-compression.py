



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

merge = a + b
seen = set()
newList = [x for x in merge if x not in seen and not seen.add(x) ]










print(merge)
print(newList)

