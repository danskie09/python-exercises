pesos = int(input("What do you have left in pesos: "))
soles = int(input("What do you have left in soles: "))
reias = int(input("What do you have left in reais: "))


total_p = pesos * 0.00025
total_s = soles * 0.29
total_r = reias * 0.18


total_usd = total_p + total_s + total_r


print("Money in USD::")
print(total_usd)