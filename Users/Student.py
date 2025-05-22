from Course import Course
from Users.user import User


class Student(User):
    def __init__(self, full_name, email, password):
        super().__init__(full_name, email, password)
        self.__full_name = full_name
        self.__email = email
        self.__password = password
        self.__matriculation_number = 0
        self.__courses = []

    def get_full_name(self):
        return self.__full_name

    def get_email(self):
        return self.__email



    def set_password(self, password):
        self.__password = password

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def set_email(self, email):
        self.__email = email


    @property
    def get_matriculation_number(self):
        return self.__matriculation_number

    def set_matriculation_number(self, matriculation_number):
        self.__matriculation_number = matriculation_number

    def add_course(self, course):
        if not isinstance(course, str):
            raise TypeError('Course must be a string')
        self.__courses.append(course)

    def get_number_of_courses_offered(self):
        return len(self.__courses)
    def get_list_of_courses_offered(self):
        return self.__courses

    def validate_password(self, password: str):
        if not isinstance(password, str):
            raise TypeError('Password must be a string')
        if password == self.__password:
            return True
        return False


