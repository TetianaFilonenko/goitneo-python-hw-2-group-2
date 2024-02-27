from task2.errors import input_error
from task2.address_book_lib import Record, AddressBook

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    name, phone = args
    new_record = Record(name)
    isvalid, message = new_record.add_phone(phone)
    if isvalid:
        book.add_record(new_record)
    return message

@input_error
def change_contact(args, book):
    # remove record by name from book and create a new record with a new phone
    # alternatively method 'change' can be implemented
    name, new_phone = args
    book.delete(name)
    new_record = Record(name)
    isvalid, message = new_record.add_phone(new_phone)
    if isvalid:
        book.add_record(new_record)
    return message

@input_error
def get_contact_phone(args, book):
    name = args[0]
    return book.find(name)

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

def get_all_contacts(book):
    return "\n".join(map(str, book.data.values()))

def main():
    book = AddressBook()
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
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(get_contact_phone(args, book))
        elif command == "all":
            print(get_all_contacts(book))
        elif command == "help":
            print_help()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
