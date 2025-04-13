import string
from operator import contains


class phoneBook:
    def __init__(self):
        self.phoneBook = {}
        self.findContact = {}

        self.counter = 0
        self.set_find_contact()

    def check_empty(self):
        if self.counter == 0:
            return True
        return False


    def add_contact(self, phone_number: str, first_name: str, last_name: str):
        if not phone_number.isnumeric():
           raise ValueError("Invalid phone number")

        if phone_number in self.phoneBook:
            raise ValueError("Phone number already in use")
        if first_name is None:
            raise ValueError("First name cannot be None")
        if last_name is None:
            raise ValueError("Last name cannot be None")

        result =(f'''
        firstname: {first_name} 
        lastname : {last_name}
        phone number: {phone_number}
        email: 
        ''')
        self.phoneBook[phone_number] = result
        self.counter += 1

        self.__set_find_contact_number(phone_number)
        self.findContact[phone_number].append(first_name)
        self.findContact[phone_number].append(last_name)

        first_name_first_letter = first_name[0].lower()
        last_name_first_letter = last_name[0].lower()
        if first_name_first_letter in self.findContact:
                self.findContact[first_name_first_letter].append([first_name, last_name, phone_number])
        if last_name_first_letter in self.findContact:
                self.findContact[last_name_first_letter].append([first_name, last_name, phone_number])

    def get_numbers_of_contact(self):
        return self.counter

    def remove_contact(self, phone_number: str):
        if phone_number  not in self.phoneBook:
            raise ValueError("Invalid phone number")

        self.phoneBook.pop(phone_number)
        if phone_number not in self.findContact:
            raise ValueError("Invalid phone number")

        name = self.findContact[phone_number]
        first_name = name[0]
        last_name = name[1]
        first_name_first_letter = first_name[0].lower()
        last_name_first_letter = last_name[0].lower()
        self.findContact.pop(phone_number)

        self.findContact[first_name_first_letter] = [contact for contact in self.findContact[first_name_first_letter] if contact[2] != phone_number]
        self.findContact[last_name_first_letter] = [contact for contact in self.findContact[last_name_first_letter] if contact[2] != phone_number]


        self.counter -= 1


    def set_email(self,phone_number, email: str):
        if phone_number not in self.phoneBook:
            raise ValueError("Invalid phone number")
        if not isinstance(email, str):
            raise ValueError("Email must be a string")
        if not ('@' in email and email.count('@') == 1)  :
            raise ValueError("Email must be a valid email address")
        if not ('.' in email and email.count('.') == 1) :
            raise ValueError("Email must be a valid email address")

        name = self.findContact[phone_number]
        result =(f'''
        firstname: {name[0]} 
        lastname: {name[1]}
        phone number : {phone_number}
        email: {email}
        ''')
        self.phoneBook[phone_number] = result


    def get_contact_by_phone_number(self, input_phone_number: str ):
        if input_phone_number in self.phoneBook:
            return self.phoneBook[input_phone_number]
        else:
            raise ValueError("Invalid phone number")

    def set_find_contact(self):
        key= "abcdefghijklmnopqrstuvwxyz0123456789!@#/\\$%^&(*-_=+)?|}]{[>.<,~`'"
        for number in key:
            self.findContact[number] = []

    def __set_find_contact_number(self, phone_number: str):
        self.findContact[phone_number] = []

    def find_by_first_name(self, first_name: str):
        first_name_first_letter = first_name[0].lower()

        match = []
        for contact in self.findContact[first_name_first_letter]:
             if contact[0].lower() == first_name.lower():
                print(f"{self.phoneBook[contact[2]]}")
                match.append(contact)

             else:
                 print("First name not found")
        return match


    def find_by_last_name(self, last_name: str):
        last_name_first_letter =last_name[0].lower()

        match = []
        for contact in self.findContact[last_name_first_letter]:
            if contact[1].lower() == last_name.lower():
                print(f"{self.phoneBook[contact[2]]}")
                match.append(contact)
            else:
                print("Last name not found")
        return match
























