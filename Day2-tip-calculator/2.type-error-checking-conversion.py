# len(12345)  # TypeError: object of type 'int' has no len()
# The above code will raise a TypeError because the len() function is used to get the length of a string, list, or other iterable objects, 
# but it cannot be used on an integer.
print(len("12345"))  # it will print 5 because it is a string and the len() function will return the number of characters in the string
print(len("3.14159"))  # it will print 7 because it is a string and the len() function will return the number of characters in the string

#check data type used type() function which will return the data type of the value passed to it as an argument

print(type("Prashant"))  # it will print <class 'str'> because it is a string
print(type(12345))  # it will print <class 'int'> because it is an integer
print(type(3.14159))  # it will print <class 'float'> because it is a float 
print(type(True))  # it will print <class 'bool'> because it is a boolean
print(type(None))  # it will print <class 'NoneType'> because it is a NoneType

# converting data type into different data type using type conversion functions
print(int("12345"))  # it will print 12345 because it is converting string "12345" to integer
print(float("3.14159"))  # it will print 3.14159 because it is converting string "3.14159" to float
print(str(12345))  # it will print "12345" because it is converting integer 12345 to string
print(bool(0))  # it will print False because it is converting integer 0 to boolean, and in Python, 0 is considered False

print(int("abc") +int("456"))  # it will raise ValueError because "abc" cannot be converted to an integer
