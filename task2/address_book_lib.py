from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if re.search(r"^[0-9]{10}$", new_value) and len(new_value) == 10:
            self.__value = new_value
        else:
            self.__value = None

    def is_valid(self):
        return bool(self.__value)

class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone: str):
        if isinstance(phone, Phone):
            phone_instance = phone
        else:
            phone_instance = Phone(phone)

        if phone_instance.is_valid():
            self.phones.append(phone_instance)
            return phone_instance.is_valid(), f'phone: {phone} was added to record {self.name.value}'
        else:
            return phone_instance.is_valid(), f'Only 10-digits numbers are accepted, you entered: {phone}'


    def remove_phone(self, phone):
        if isinstance(phone, Phone):
            phone = phone.value
        self.phones = [el for el in self.phones if el.value != phone]


    def edit_phone(self, old_phone, new_phone):
        if isinstance(old_phone, Phone) and isinstance(new_phone, Phone):
            old_phone = old_phone.value
            new_phone = new_phone.value

        self.phones = [Phone(new_phone) if el.value == old_phone else el for el in self.phones ]

    def find_phone(self, phone):
        if isinstance(phone, Phone):
            phone = phone.value
        for _i in filter(lambda el: phone == el.value, self.phones):
            return f"{self.name} has {phone} in phone list\n{str(self)}"
        return f"{self.name} doen't have {phone} in phone list\n{str(self)}"

    def __str__(self):
        return f"Contact name: {self.name}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def find(self, name: str):
        for key, value in filter(lambda el: name == el[0], self.items()):
            return f"Found record with name: '{key}'. \nResult: {str(value)}"

    def add_record(self, record: Record):
        if self.data.get(record.name.value, -1) == -1:
            self.data[record.name.value] = record
        else:
            record.phones += self.data[record.name.value].phones
            self.data[record.name.value] = record
        return record

    def delete(self, name: str):
        del self.data[name]
