bmi =84 /1.65 **2
print(f"Your BMI is {bmi}") # it will print Your BMI is 30
print(int(bmi)) # it will print 30 because it is converting the float value of bmi to an integer, and in this case, it will truncate the decimal part and return only the whole number
print(round(bmi)) # it will print 30 because it is rounding the value of bmi to the nearest integer
print(round(bmi,2)) # it will print 30.86 because it is rounding the value of bmi to 2 decimal places


score = 0
score += 1 # it will add 1 to the score variable and update its value to 1
print(score) # it will print 1 because the score variable has been updated to 1

score *= 2 # it will multiply the score variable by 2 and update its value to 2
print(score) # it will print 2 because the score variable has been updated to 2

score /= 2 # it will divide the score variable by 2 and update its value to 1
print(score) # it will print 1.0 because the score variable has been updated to



# f strinf is a string that is prefixed with the letter 'f' or 'F' and allows you to embed expressions inside string literals, using curly braces {}.
# The expressions inside the curly braces are evaluated at runtime and their values are inserted into the string

score =0
height = 2.5
isWinning = True

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}") # it will print Your score is 0, your height is 2.5, you are winning is True because it is using f-string to embed the values of score, height, and isWinning variables into the string literal.



print( 6 + 4 / 2 - ( 1 * 2 ) ) # it will print 6.0 because it is following the order of operations according to PEMDAS,
# first it will perform the multiplication, then it will perform the division, 
# then it will perform the addition and subtraction from left to right.
