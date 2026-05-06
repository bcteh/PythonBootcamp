
height = 0.0
weight = 0.0

while True:
    try:
        # Prompt user and convert input to an float
        height = float(input("Enter your height in meters (not less than 1.00 meter): "))
        
        # Check if the number meets the criteria
        if height >= 1.0:
            print(f"Thank you! Your height is {height} meter.")
            break # Exit the loop if valid
        else:
            print("Height is less than 1.0 meter. Please try again.")
    except ValueError:
        # Handle non-integer inputs
        print("Invalid input. Please enter a valid height.")

while True:
    try:
        # Prompt user and convert input to an float
        weight = float(input("Enter your weight in kilograms (not less than 1.0 kg): "))
        
        # Check if the number meets the criteria
        if weight >= 1.0:
            print(f"Thank you! Your weight is {weight} kg.")
            break # Exit the loop if valid
        else:
            print("Weight is less than 1.0 kg. Please try again.")
    except ValueError:
        # Handle non-integer inputs
        print("Invalid input. Please enter a valid weight.")

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}. You are underweight.")   
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi:.2f}. You are normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi:.2f}. You are overweight.")
else:
    print(f"Your BMI is {bmi:.2f}. You are obese.") 