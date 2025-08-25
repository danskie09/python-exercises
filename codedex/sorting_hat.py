Gryffindor = 0;
Ravenclaw = 0;
Hufflepuff = 0;
Slytherin = 0;


q1 = int(input("Q1) Do you like Dawn or Dusk\n 1. Dawn\n 2.Dusk"))
if q1 == 1:
    Gryffindor += 1
    Ravenclaw += 1

elif q1 == 2:
    Slytherin += 1;
    Hufflepuff += 1;
else:
    print("Wrong Input")
    


q2 = int(input("Q2) When I’m dead, I want people to remember me as: \n 1. The Good \n 2. The Great \n3. The Wise\n 4.The Bold"))
if q2 == 1:
    Hufflepuff += 2;
elif q2 == 2:
    Slytherin += 2;
elif q2 == 3:
    Ravenclaw += 2;
elif q2 == 4:
    Gryffindor += 2;
else:
    print("Wrong Input")
    
q3 = int(input("Q3) Which kind of instrument most pleases your ear? \n 1. The Violin \n 2. The Trumphet \n 3. The Piano \n 4. The Drum"))

if q3 == 1:
    Slytherin += 4
elif q3 == 2:
    Hufflepuff += 4
    
elif q3 == 3:
    Ravenclaw += 4
elif q3 == 4:
    Gryffindor += 4;
else:
    print("Wrong Input")
    


print(f"The Scores:\n {Gryffindor}\n {Ravenclaw} \n {Hufflepuff} \n {Slytherin}")
