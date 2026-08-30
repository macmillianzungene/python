# Collect two numbers safely as floats
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Basic operations
addition = round(num1 + num2,)
subtraction = round(num1 - num2,)
multiplication = round(num1 * num2,)
division = round(num1 / num2, 2)

# Division-based operations need a zero check
if num2 == 0:
    floor_division = "Error: Cannot divide by zero"
    modulus = "Error: Cannot divide by zero"
else:
    division = round(num1 / num2, 2)
    floor_division = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)

# Display results in a formatted table
print("\n----- Calculator Results -----")
print(f"{'Operation':<20}{'Result'}")
print("-" * 30)
print(f"{'Addition (+)':<20}{addition}")
print(f"{'Subtraction (-)':<20}{subtraction}")
print(f"{'Multiplication (*)':<20}{multiplication}")
print(f"{'Division (/)':<20}{division}")
print(f"{'Floor Division (//)':<20}{floor_division}")
print(f"{'Modulus (%)':<20}{modulus}")