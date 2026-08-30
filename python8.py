# How if/else and elif works
age = input("Enter age: ")

age = int(age)
_pass = input("Do you have have the pass? (yes/no) ").lower()

if age >= 18 and _pass == "yes":
    print("Access granted to VIP!")
elif age >= 18:
    print("Access granted to general area!") 
else:
    print("Access denied!")