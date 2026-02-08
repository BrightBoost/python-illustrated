# Create the dictionary with names as keys and phone numbers as values
contacts = {
    "John": "123-456-7890",
    "Jane": "987-654-3210",
    "Mike": "555-123-4567"
}

# Add a new contact
contacts["Imke"] = "123-978-6543"

# Check if "Maaike" exists in the dictionary, and if not, add her
if "Maaike" not in contacts:
    contacts["Maaike"] = "444-555-6666"

# Delete one of the contacts
contacts.pop("Imke", None)

# Print all the names in the dictionary
print("Names in contacts:", list(contacts.keys()))



