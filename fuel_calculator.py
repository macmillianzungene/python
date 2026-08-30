
# This estimates how much a trip will cost based on distance and petrol price.

# input how many kilometers they want to drive
kilometers = float(input("Enter the distance you want to drive (km): "))

# input for the current petrol price per liter
petrol_price = float(input("Enter the petrol price per liter (R): "))

# Car uses 1 liter per 10 km
liters_needed = kilometers / 10

# Calculate total cost
total_cost = liters_needed * petrol_price
total_cost = round(total_cost, 2)
liters_needed = round(liters_needed, 2)

# Displaying results
print("\n----- Fuel Cost Estimate -----")
print(f"Distance: {kilometers} km")
print(f"Fuel needed: {liters_needed} liters")
print(f"Petrol price: R{petrol_price} per liter")
print(f"Total estimated cost: R{total_cost}")