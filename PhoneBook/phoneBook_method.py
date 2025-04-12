import string
from operator import contains


class phoneBook:
    def __init__(self):
        self.phoneBook = {}
        self.findContact = {}
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
        result =(f'''
        firstname: {self.firstName} 
        lastname : {self.lastName}
        phone number: {phone_number}
        email: {self.email}
        ''').strip('\n')
        self.phoneBook[phone_number] = result
        self.counter += 1
        for key in self.findContact.keys():
            if first_name[0] == key:
                self.findContact[key] = first_name + " " + last_name
            if last_name[0] == key:
                self.findContact[key] = first_name + " " + last_name


    def get_numbers_of_contact(self):
        return self.counter

    def remove_contact(self, phone_number: str):
        if phone_number in self.phoneBook:
            self.phoneBook.pop(phone_number)


    def set_email(self,phone_number, email: str):
        if phone_number not in self.phoneBook:
            raise ValueError("Invalid phone number")
        if not isinstance(email, str):
            raise ValueError("Email must be a string")
        if not ('@' in email and email.count('@') == 1)  :
            raise ValueError("Email must be a valid email address")
        if not ('.' in email and email.count('.') == 1) :
            raise ValueError("Email must be a valid email address")


        result =(f'''
        firstname: {self.firstName} 
        lastname: {self.lastName}
        phone number : {phone_number}
        email: {email}
        ''').strip('\n')
        self.phoneBook[phone_number] = result







    def get_contact_by_phone_number(self, input_phone_number: str ):
        if input_phone_number in self.phoneBook:
            return self.phoneBook[input_phone_number]
        else:
            raise ValueError("Invalid phone number")

    def set_find_contact(self):
        key= "abcdefghijklmnopqrstuvwxyz"
        for number in key:
            self.findContact[number] = []



















