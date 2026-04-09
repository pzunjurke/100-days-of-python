print("Welcome to Rollercoster!")
height=int(input("what is your heigh in cm? "))
if height >= 120:
    age = int(input("what is your age? "))
    if age < 12:
        print("you have to pay $5")
    elif age <= 18:
        print("you have to pay $7")
    else:
        print("you have to pay $12")
else:
    print("you can ride the rollercoster!")


#  you can put if/else statements inside if/else statements, this is called nested if/else statements
