def parse_input(user_input):
    command, *args = user_input
    return command.strip().lower(), *args

def add_contact(name,phone):
    contact = {"name":name, "phone":phone}
    return contact

def change_contact(name,phone,contacts):
    for contact in contacts:
        if contact["name"] == name:
            contact["phone"] = phone
            return True

def show_phone(name,contacts):
    for contact in contacts:
        if contact["name"] == name:
            return contact["phone"]
    return "Contact not found"

def show_all(contacts):
    str_contacts = ""
    for contact in contacts:
        str_contacts += f"Name: {contact['name']}, Phone: {contact['phone']}\n"
    return str_contacts
