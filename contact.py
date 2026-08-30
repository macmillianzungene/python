# The Phone Directory Search
# A simple contact lookup using a dictionary of names and phone numbers.

# 1. Dictionary of contacts: name -> phone number (kept as strings)
contacts = {
    "Thandiwe": "0821112222",
    "Sipho": "0837654321",
    "Aisha": "0794445555"
}

# 2. Ask the user for the name they want to look up
search_name = input("Enter the name of the friend you want to look up: ").strip()

# 3. Check if the name exists as a key in the dictionary
if search_name in contacts:
    number = contacts[search_name]
    print(f"Found! {search_name}'s number is {number}")
else:
    # 4. Name not found
    print("Contact not found.")