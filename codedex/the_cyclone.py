height = int(input("Please input your height: "))


credit = int(input("Please input your credits: "))


if height > 137 and credit >= 10:
    print("Enjoy the ride!")
elif height < 137 and credit >= 10:
    print("You are not tall enough")
elif height >= 137 and credit < 10:
    print("You dont have enough credits")
else:
    print("You have not met the requirements")