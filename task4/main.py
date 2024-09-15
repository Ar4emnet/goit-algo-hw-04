import function_bot

def main():
    contacts = []
    print("Welcome to the assistant bot")

    while True:
        command = input("Enter a command: ").split()
        command, *args = function_bot.parse_input(command)

        if command == "add":
            try:
                contacts.append(function_bot.add_contact(args[0], args[1]))
                print("Contact added")
            except IndexError:
                print("Usage: add <name> <phone>")

        elif command == "hello":
            print("How can I help you?")

        elif command == "change":
            try:
                if function_bot.change_contact(args[0], args[1], contacts):
                    print("Contact updated")
                else:
                    print("Contact not found")
            except IndexError:
                print("Usage: change <name> <phone>")

        elif command == "phone":
            try:
                print(args[0], function_bot.show_phone(args[0], contacts))
            except IndexError:
                print("Usage: phone <name>")
        elif command == "all":
            function_bot.show_all(contacts)

        elif command in ["exit", "close"]:
            print("Goodbye!")
            break
        else: print("Invalid command")

if __name__ == "__main__":
    main()


