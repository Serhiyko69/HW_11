from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value


class Phone(Field):
    def set_value(self, value):
        if self.is_valid_phone(value):
            super().set_value(value)
        else:
            raise ValueError("Invalid phone number")

    def is_valid_phone(self, value):

        return True


class Birthday(Field):
    def set_value(self, value):
        if self.is_valid_birthday(value):
            super().set_value(value)
        else:
            raise ValueError("Invalid birthday")

    def is_valid_birthday(self, value):

        return True


class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Field(name)
        self.phone = Phone(phone) if phone else None
        self.birthday = Birthday(birthday) if birthday else None

    def days_to_birthday(self):
        if self.birthday:
            today = datetime.now()
            next_birthday = datetime(today.year, self.birthday.value.month, self.birthday.value.day)
            if today > next_birthday:
                next_birthday = next_birthday.replace(year=today.year + 1)
            days_left = (next_birthday - today).days
            return days_left
        else:
            return None


class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def __iter__(self):
        return self.RecordIterator(self)

    class RecordIterator:
        def __init__(self, address_book):
            self.address_book = address_book
            self.index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.index < len(self.address_book.records):
                record = self.address_book.records[self.index]
                self.index += 1
                return record
            else:
                raise StopIteration


# Приклад використання:
address_book = AddressBook()
record1 = Record("Ivan Ivanov", phone="0965996655", birthday=datetime(1990, 5, 15))
record2 = Record("Olena Teliga", phone="0956543210")
address_book.add_record(record1)
address_book.add_record(record2)

for record in address_book:
    print(record.name.get_value())
    if record.phone:
        print("Phone:", record.phone.get_value())
    if record.birthday:
        print("Days to birthday:", record.days_to_birthday())
    print()
