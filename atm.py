# The Smart ATM Withdrawal Simulator that s
# 
# 
# imulates a basic bank withdrawal, checking for valid amounts and sufficient funds.

# Fixed starting balance
balance = 500

# Ask user how much they want to withdraw
withdrawal_amount = float(input("Enter the amount you want to withdraw: R"))

# Check if withdrawal is valid and within balance
if withdrawal_amount <= 0:
    print("Invalid amount. You must withdraw more than R0.")
elif withdrawal_amount <= balance:
    balance = balance - withdrawal_amount
    print(f"Withdrawal successful! Remaining balance: R{balance}")
else:
    print("Declined. Insufficient funds")