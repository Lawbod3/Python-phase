import string
from operator import contains


class phoneBook:
    def __init__(self):
        self.phoneBook = {}
        self.findContact = []
        self.phoneNumber = ""
        self.firstName = ""
        self.lastName = ""
        self.email = ""
        self.counter = 0

    def check_empty(self):
        if self.counter == 0:
            return True
        return False


    def add_contact(self, phone_number: str, first_name: str, last_name: str):
        if not phone_number.isnumeric():
           raise ValueError("Invalid phone number")
        self.phoneNumber = phone_number
        self.firstName = first_name
        self.lastName = last_name
        result = (f'''
        firstname: {self.firstName} 
        lastname : {self.lastName}
        phone number: {phone_number}
        email: {self.email}
        ''')
        self.phoneBook[phone_number] = result
        self.counter += 1

    def get_numbers_of_contact(self):
        return self.counter

    def remove_contact(self, phone_number: str):
        if phone_number in self.phoneBook:
            self.phoneBook.pop(phone_number)


    def set_email(self, email: str):
        if not isinstance(email, str):
            raise ValueError("Email must be a string")
        if  '@' in email and email.count('@') == 1 and '.'  in email.split('@')[1]:
            self.email = email
        else:
            raise ValueError("Email must be a valid email address")



    def get_contact_by_phone_number(self, input_phone_number: str ):
        if input_phone_number in self.phoneBook:
            return self.phoneBook[input_phone_number]
        else:
            raise ValueError("Invalid phone number")











