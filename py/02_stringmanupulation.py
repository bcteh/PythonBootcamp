name ="Din"
age = 38
Text1 = "Hello, World!"
Text2 = """Python is great! You can do a lot of things with it."""

print(name)
print(type(name))
print(age)
print(type(age))

print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
print("My name is %s and I am %d years old." % (name, age))
print(Text1)
print(Text2)
print(' ')

print(Text2[0:6])  # Slicing
print(Text2[7:12])  # Slicing 
print(' ')

Text3 = """Python is great! You can do a lot of things with it."""

Length_of_Text3 = len(Text3)
print(f"Length of the string Text3 is {Length_of_Text3}.")  # Length of the string
print(' ')
#print(Text3.count("a"))  # Count occurrences of "a"
print(f"Count occurrences of a is {Text3.count('a')}.") 
print(' ')
print(f"Count occurrences of Python is {Text3.count('Python')}.") 
print(' ')
print(Text3.upper())  # Convert to uppercase