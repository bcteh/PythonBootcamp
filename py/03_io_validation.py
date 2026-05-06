while True:
    try:
        # Prompt user for name and convert input to a string
        name1 = str(input("Enter your name : "))
        
        # Check if the name is valid (non-empty)
        if len(name1) >= 1:
            print(f"Thank you! You entered: {name1}")
            break # Exit the loop if valid
        else:
            print("Name is less than 1 character. Please try again.")
    except ValueError:
        # Handle non-integer inputs
        print("Invalid input. Please enter a valid name.")

while True:
    try:
        # Prompt user and convert input to an float
        height = float(input("Enter your height in meters (not less than 1.0 meter): "))
        
        # Check if the number meets the criteria
        if height >= 1.0:
            print(f"Thank you! Your name is {name1} and height is {height} meters.")
            break # Exit the loop if valid
        else:
            print("Height is less than 1.0 meter. Please try again.")
    except ValueError:
        # Handle non-integer inputs
        print("Invalid input. Please enter a valid height.")


while True:
    try:
        # Prompt user and convert input to an integer
        age = int(input("Enter your age (not less than 18): "))
        
        # Check if the number meets the criteria
        if age >= 18:
            print(f"Thank you! Your name is {name1} and age is {age} years old and height is {height} meters.")
            break # Exit the loop if valid
        else:
            print("Age is less than 18. Please try again.")
    except ValueError:
        # Handle non-integer inputs
        print("Invalid input. Please enter a valid age.")