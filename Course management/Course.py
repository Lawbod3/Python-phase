from Users.facilitator import Facilitator


class Course(object):
    def __init__(self, course_name, code, facilitator:Facilitator):
        self.__validate_course(course_name, code, facilitator)
        self.__course_name = course_name
        self.__facilitator = facilitator
        self.__code = code
        self.__score = {}
        self.__students = []


    def get_course_name(self):
        return self.__course_name

    def get_facilitator_name(self):
        return self.__facilitator.get_full_name()

    def get_facilitator_id(self):
        return self.__facilitator.get_id()

    def get_code(self):
        return self.__code

    def set_students(self, student):
        if student not in self.__students:
           self.__students.append(student)
        else:
            raise ValueError("student already registered")

    def set_score(self, score, number):
        for student in self.__students:
            if student.get_matriculation_number == number:
                self.__score[number] = score
                return

        raise ValueError("Student not enrolled in course")
    def get_scores(self, number):
        return self.__score.get(number)





    def __validate_course(self,course_name, code, facilitator:Facilitator):
        if not isinstance(course_name, str):
            raise TypeError("The course name must be a string")
        if not isinstance(code, str):
            raise TypeError("The course code must be a string")
        if not isinstance(facilitator, Facilitator):
            raise TypeError("The facilitator must be an instance of Facilitator")
