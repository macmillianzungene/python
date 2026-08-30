# Command-Line Contact Book and Stores contacts as a list of dictionaries and lets the user 
# add, search, view, and delete contacts via a menu.

contacts = []


def add_contact():
    """Ask the user for contact details and append a new dictionary to the list."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(new_contact)
    print(f"\nContact '{name}' added successfully.")


def search_contact(name):
    """Search contacts by name (case-insensitive). Return the matching dict or None."""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def delete_contact(name):
    """Remove a contact by name. Print feedback on whether it was found/removed."""
    contact = search_contact(name)
    if contact:
        contacts.remove(contact)
        print(f"\nContact '{name}' deleted successfully.")
    else:
        print(f"\nNo contact found with the name '{name}'.")


def view_all():
    """Display all contacts in a formatted layout."""
    if not contacts:
        print("\nNo contacts saved yet.")
        return

    print("\n===== ALL CONTACTS =====")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print("-" * 25)


def main():
    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_name = input("Enter the name to search for: ").strip()
            result = search_contact(search_name)
            if result:
                print(f"\nContact found:")
                print(f"Name: {result['name']}")
                print(f"Phone: {result['phone']}")
                print(f"Email: {result['email']}")
            else:
                print(f"\nNo contact found with the name '{search_name}'.")
        elif choice == "3":
            delete_name = input("Enter the name to delete: ").strip()
            delete_contact(delete_name)
        elif choice == "4":
            view_all()
        elif choice == "5":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option. Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()