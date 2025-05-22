from Course import Course
from Users.Student import Student
from Users.facilitator import  Facilitator
from Users.user import User


class CourseManagement:
    def __init__(self):
        self.__courses = []
        self.__users = []
        self.__matriculation_generator = 1000
        self.__id_generator = 0

    def register(self, user: User):
        if not isinstance(user, User):
            raise TypeError("User must be of type User")

        if isinstance(user, Facilitator):
            if user not in self.__users:
               user.set_id(self.__generate_facilitation_id())
               self.__users.append(user)
        elif isinstance(user, Student):
            if user not in self.__users:
               user.set_matriculation_number(self.__generate_matriculation_number())
               self.__users.append(user)


        return  user

    def register_course(self, course_name, course_code, facilitator: Facilitator):
        self.__validate_course_registration(course_name, course_code, facilitator)
        for course in self.__courses:
            if course.get_code().lower() == course_code.lower():
                raise ValueError("Course code already exists")
        new_course = Course(course_name=course_name, code=course_code, facilitator=facilitator)
        self.__courses.append(new_course)
        return new_course

    def course_available(self):
        return len(self.__courses)

    def enroll_student_to_course(self, student: Student, course_code: str):
        if not isinstance(student, Student):
            raise TypeError("Student must be of type Student")
        if student not in self.__users:
            raise ValueError("Student is not in the users list")
        for course in self.__courses:
            if course.get_code().lower() == course_code.lower():
                course.set_students(student)
                student.add_course(course.get_course_name())
                return
        raise ValueError("course is not in the courses list")

    def __validate_course_registration(self, course_name: str, course_code: str, facilitator: Facilitator):
        if not isinstance(course_name, str):
            raise TypeError("Course name must be of type str")
        if not isinstance(facilitator, Facilitator):
            raise TypeError("Facilitator must be of type Facilitator")
        if not isinstance(course_code, str):
            raise TypeError("Course code must be of type str")
        if facilitator not in self.__users:
            raise ValueError("Facilitator is already in self.__users")

    def view_course_facilitator(self, course_code: str):
        if not isinstance(course_code, str):
            raise TypeError("Course code must be of type str")
        for course in self.__courses:
            if course.get_code().lower() == course_code.lower():
                return course.get_facilitator_name()
        return None

    def set_course_scores(self, course_code, facilitator_id: int, score, student_matriculation_number: int):
        self.__validate_course_and_facilitator(course_code, facilitator_id, student_matriculation_number)
        for course in self.__courses:
            if course.get_code().lower() == course_code.lower() and facilitator_id == course.get_facilitator_id():
                course.set_score(score, student_matriculation_number)
                return "Score set successfully"
        return "Invalid course code or facilitator id doesn't match course code"

    def __validate_course_and_facilitator(self,  course_code: str, facilitator_id: int, student_matriculation_number: int):
        if not isinstance(course_code, str):
            raise TypeError("Course code must be of type str")
        if not isinstance(facilitator_id, int):
            raise TypeError("Facilitator id must be of type int")
        if not isinstance(student_matriculation_number, int):
            raise TypeError("Student matriculation number must be of type int")
        facilitator_exist = False
        for user in self.__users:
            if isinstance(user, Facilitator):
               if  user.get_id() == facilitator_id:
                   facilitator_exist = True
                   break
        if not facilitator_exist:
            raise ValueError("Facilitator does not exist")
        student_exist = False
        for user in self.__users:
            if isinstance(user, Student) and user.get_matriculation_number == student_matriculation_number:
                student_exist = True
                break
        if not student_exist:
            raise ValueError("Student does not exist")



    def get_course_result(self, course_code, matriculation_number):
        if not isinstance(course_code, str):
            raise TypeError("Course code must be of type str")
        if not isinstance(matriculation_number, int):
            raise TypeError("Matriculation id must be of type int")
        for course in self.__courses:
            if course.get_code().lower() == course_code.lower():
                score = course.get_scores(matriculation_number)
                if  score is not None:
                    return score
                else:
                    return "yet to be uploaded"
        return "Invalid course code or Matriculation number doesn't match course code"

    def get_course_management_users(self):
        return self.__users

    def get_list_of_courses(self):
        result = []
        for course in self.__courses:
            result.append(course.get_code())
        return result

    def __generate_facilitation_id(self):
        self.__id_generator += 1
        return self.__id_generator

    def __generate_matriculation_number(self):
        self.__matriculation_generator += 1
        return self.__matriculation_generator

    def verify_user(self, identity_number, password):
        for user in self.__users:
            if isinstance(user, Facilitator):
               if identity_number == user.get_id():
                   if user.validate_password(password) is True:
                      return True
            if isinstance(user, Student):
               if identity_number == user.get_matriculation_number:
                    if user.validate_password(password) is True:
                        return True
        return False

