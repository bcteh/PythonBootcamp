# test error handling by input a number and divide 10 by that number
try:
    num = int(input("Enter a number to divide 10 by: "))
    result = 10 / num
    print(f"10 divided by {num} is: {result}")  
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid integer!")



#error handling with multiple exceptions
try:    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"{num1} divided by {num2} is: {result}") 
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid integer!")

