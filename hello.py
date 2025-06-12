

import random



a = random.sample(range(1,101), 12)

b = random.sample(range(1,101), 12)


print(a)
print(b)





mergeList = a + b



seen = set()

duplicates = set()

for items in mergeList:
    if items in seen:
        duplicates.add(items)
    else:
        seen.add(items)



print(list(seen))



