from abc import ABC , abstractmethod

class User(ABC):
    def __init__(self, full_name,  email, password):
        self.__full_name = full_name

        self.__email = email
        self.__password = password
    @property
    @abstractmethod
    def get_full_name(self):
        return self.__full_name



    @property
    @abstractmethod
    def get_email(self):
        return self.__email



    @abstractmethod
    def set_password(self, password):
        self.__password = password


    @abstractmethod
    def set_full_name(self, full_name):
        self.__full_name = full_name


    @abstractmethod
    def set_email(self, email):
        self.__email = email

    @abstractmethod
    def validate_password(self, password: str):
        if password == self.__password:
            return True
        return False


