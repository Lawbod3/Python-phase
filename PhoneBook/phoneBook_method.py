class phoneBook:
    def __init__(self):
        self.phoneBook = {}
        self.findContact = []
        self.phoneNumber = ""
        self.firstName = ""
        self.lastName = ""


    def add_contact(self, phone_number: str, first_name: str, last_name: str):
        if not phone_number.isnumeric():
           raise ValueError("Invalid phone number")
        self.phoneNumber = phone_number
        if not isinstance(first_name, str):
            raise ValueError("First name must be a string")
        self.firstName = first_name
        if not isinstance(last_name, str):
            raise ValueError("Last name must be a string")
        self.lastName = last_name

        self.phoneBook[self.phoneNumber] = self.firstName + " " + self.lastName

    def get_phone_number(self):
        return self.phoneNumber

    def get_first_name(self):
        return self.firstName

    def get_last_name(self):
        return self.lastName






