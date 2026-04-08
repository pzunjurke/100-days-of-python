# make the line of code run without any error and print the output

print("Number of letters in yourname : " + str(len(input("Enter your name "))))


 # it will raise TypeError because len() function cannot be used on an integer, and input() function returns a string, so we need to convert it to an integer before using len() function