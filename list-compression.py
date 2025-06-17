x = [1, 2, 3]
y = [5, 10, 15]

allProducts = []
oddProducts = []

for a in x:
    for b in y:
        allProducts.append(a*b)
        product = a*b
        if product % 2 != 0:
            oddProducts.append(product)






print(allProducts)
print(oddProducts)