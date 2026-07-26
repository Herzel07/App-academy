# CONTACT BOOK PROGRAM
# REQUIREMENT 1:
# Create an empty list to store all contacts.
# Each contact added later will be a dictionary.
contacts = []

# REQUIREMENT 2:
# Create a function that adds a new contact.
def add_contact():

# Ask the user for the contact details.
# Phone numbers stay as strings because they may begin with 0.
name = input("Enter name: ")
phone = input("Enter phone number:
email = input("Enter email: ")

# Store one person's details in a dictionary.
# The words on the left are keys. 
# The variables on the right contain user's information.
contact = {

"name": name
"phone": phone
"email": emai
}

# Add the new contact dictionary 
#to the end of the contacts list. 
contacts.append(contact)

print("Contact added successfully!")

# REQUIREMENT 3:
# Create a function that searches for a contact by name.
# The name inside the brackets is information passed into the function.
def search_contact(name):

# Go through the contacts list one contact at a time. 
for contact in contacts:

# Get the name from the current dictionary and compare it 
# with the name being searched for.
# .lower() allows "ASIVE", "Asive" and "asive" to match.
if contact["name"].lower() ==
      name.lower():

# Give back the matching contact dictionary.
return contact

# This runs only if the loop finishes without finding a match.
return None

# REQUIREMENT 4:
# Create a function that deletes a contact by name.
def delete_contact(name):

# Reuse the search function to find the contact first.
contact = search_contact(name)

# If a contact dictionary was found, remove it from the list.
if contact:
    contacts.remove(contact)
     print("Contact deleted successfully!")


# If search_contact() returned None, the contact was not found.
else:
    print("Contact not found.")


# REQUIREMENT 5:
# Create a function that displays every saved contact.
def view_all():



# len() counts the number of items in the contacts list.
# If the number is 0, the contact book is empty.

if len(contacts) == 0:
     print("No contacts available."

else:
    print("\n----- CONTACT LIST
-----")


display

# Go through the list and one contact at a time.

for contact in contacts: 
     print(f"Name :
{contact['name']}")

        print(f"Phone:
{contact['phone']}")

        print(f"Email:
{contact['email']}")


# Print 25 dashes to separate the contacts.
   print("-" * 25)


# REQUIREMENT 6:
# Create a menu that keeps running until the user chooses Exit.
while True:

         print("\n===== CONTACT BOOK =====") 
         print("1. Add Contact")
         print("2. Search Contact")
         print("3. Delete Contact")
         print("4. View All Contacts")
         print("5. Exit")


# Ask the user which action they want to perform.
# The choice is stored as text,
#so we compare it with "1", "2", etc.
      choice = input("Choose an option: ")


# OPTION 1:
# Call the function that adds a contact.
if choice == "1":
    add_contact()


# OPTION 2:

# Ask for a name, search for it and

elif choice == "2": 
       name = input("Enter contact name to search: ")
result = search_contact(name)


# If result contains a

dictionary,

display the contact.

if result:
    print("\nContact found:")
    print(f"Name
{result['name']}") 
    print(f"Phone:
{result['phone']}")
    print(f"Email:
{result['email']}")


# If result is None, no contact the name.
else:
    print("Contact not found.")


# OPTION 3:
# Ask which contact must be deleted,
# then call the delete function.
elif choice == "3":
     name = input("Enter contact name to delete: ")
          delete_contact(name)


# OPTION 4:
# Call the function that displays contacts.
elif choice == "4":
         view_all()


# OPTION 5:
# Stop the while loop and end the pro
elif choice == "5": 
       print("Goodbye!")
             break

# This runs if the user enters something other than 1 to 5.
else:
   print("Invalid option. Please choose from 1 to 5.")
