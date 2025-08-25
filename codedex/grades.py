grade = int(input("Please enter the grade: "))



if grade < 0 & grade > 100:
    print("Invalid Input")
elif grade >= 55:
    print("You passed!")
else:
    print("You failed")