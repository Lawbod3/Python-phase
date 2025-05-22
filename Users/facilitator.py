from Users.user import User


class Facilitator(User):
    def __init__(self, full_name,  email, password):
        super().__init__(full_name,  email, password)
        self.__full_name = full_name
        self.__email = email
        self.__password = password
        self.__id = 0
        self.__courses_offered = []

    def get_full_name(self):
        return self.__full_name

    def get_id(self):
        return self.__id

    def get_email(self):
        return self.__email




    def set_password(self, password):
        self.__password = password

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def set_id(self, id):
        self.__id = id

    def set_email(self, email):
        self.__email = email

    def validate_password(self, password: str):
        if not isinstance(password, str):
            raise TypeError('Password must be a string')
        if password == self.__password:
            return True
        return False


