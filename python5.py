# Username and Message Formatter

# Collect input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio = input("Enter a short bio message: ")

# Create username: first initial + last name, all lowercase
username = (first_name[0] + last_name).lower()

# Full name in Title Case
full_name = f"{first_name} {last_name}".title()

# Clean up bio: strip whitespace, then replace 'I am' with 'I'm'
clean_bio = bio.strip()
clean_bio = clean_bio.replace("I am", "I'm")

# Character count (based on the cleaned bio)
bio_length = len(clean_bio)

# Display formatted profile
print("\n----- User Profile -----")
print(f"Username: {username}@mcbuddy.co.za")
print(f"Full Name: {full_name}")
print(f"Bio: {clean_bio}")
print(f"Bio Length: {bio_length} characters")