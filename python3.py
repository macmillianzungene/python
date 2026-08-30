# A professional system email generator using f strings

first = input("Enter Frist Name: ").strip()
last = input("Enter Last Name: ").strip()

username = f"{first[0]}{last}"
print(f"Your email is: {username.lower()}@gmail.com")