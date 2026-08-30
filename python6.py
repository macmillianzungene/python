# lets calculate the tip
bill = float(input("Enter the amount: R"))
tip = 0.15

value_tip = bill * tip
total_cost = bill + value_tip

print(f"Tip here: {value_tip,}")
print(f"Tip here: {round(value_tip, 2)} rounded")

print(f"Total cost: {total_cost,}")
print(f"Total cost: {round(total_cost, 2)} rounded")