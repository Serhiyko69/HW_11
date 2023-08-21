from datetime import datetime

class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.validate(val)
        self.__value = val

    def validate(self, value):
        pass

class Phone(Field):
    def validate(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Invalid phone number")

class Birthday(Field):
    def get_date(self):
        return datetime.strptime(self.value, '%Y-%m-%d')
class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = Field(name)
        self.phone = Phone(phone) if phone else None
        self.birthday = Birthday(birthday) if birthday else None

    def days_to_birthday(self):
        if self.birthday and self.birthday.value:
            today = datetime.now()
            next_birthday = datetime(today.year, self.birthday.get_date().month, self.birthday.get_date().day)
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

address_book = AddressBook()
record1 = Record("Ivan Ivanov", phone="0965996655", birthday="1990-05-15")
record2 = Record("Olena Teliga", phone="0956543210")
address_book.add_record(record1)
address_book.add_record(record2)

for record in address_book:
    print(record.name.value)
    if record.phone:
        print("Phone:", record.phone.value)
    if record.birthday:
        print("Days to birthday:", record.days_to_birthday())
    print()