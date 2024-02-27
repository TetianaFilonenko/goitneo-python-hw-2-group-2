class DuplicateError(BaseException):
    """Contact has been already added"""
class NotFoundError(BaseException):
    """Contact has not been found"""

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "No argument for contact name was provided"
        except KeyError:
            return "Name can't be found in contacts"
        except DuplicateError:
            return "Contact was not added. Same contact was added before. You can use change command"
        except NotFoundError:
            return f"Contact with name is not present in our system"

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if contacts.get(name, -1) == -1:
        contacts[name] = phone
        return "Contact added."
    else:
        raise DuplicateError


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if contacts.get(name, -1) == -1:
        raise NotFoundError
    else:
        contacts[name] = new_phone
        return "Contact phone number was changed."

@input_error
def get_contact_phone(args, contacts):
    name = args[0]
    if contacts[name]:
        # Alternatively custom error `NotFoundError` can be raised here if contacts.get(name, -1) == -1
        return f"Contact with name: {name} has phone number: {contacts[name]}"

def print_help():
    help_text = """
Available commands:
  hello                - Ask the bot how it can help you.
  add [name] [phone]   - Adds a contact with the specified name and phone number.
  change [name] [phone]- Changes the phone number for the specified contact.
  phone [name]         - Retrieves the phone number for the specified contact.
  all                  - Displays all contacts in the system.
  help                 - Shows this help message.
  close/exit           - Exits the program.
"""
    print(help_text)

def get_all_contacts(contacts):
    result = []
    for name, phone in contacts.items():
        result.append(f"Contact with name: {name} has phone number: {phone}")
    return ("\n").join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact_phone(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        elif command == "help":
            print_help()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
