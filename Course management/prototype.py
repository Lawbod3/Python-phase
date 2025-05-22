import re

from Users.Student import Student
from Users.facilitator import Facilitator
from Users.user import User
from course_management import CourseManagement

full_name = ""
email = ""
password = ""

def validat_input(value: str):
    if re.fullmatch(r"^[A-Z,a-z ]+$", value) and len(value) > 3:
        return True
    return False

def validate_email(value: str):

    email = r'^[a-zA-Z0-9_-]{2,30}@gmail\.com$'
    if re.fullmatch(email, value):
        return True
    else:
        return False

def valid_code(value: str):
    if re.fullmatch(r"^[A-Za-z0-9]+$", value) and len(value) > 6:
        return True
    return False


def main():
    admin = CourseManagement()
    while True:
        print("""
            === Course Management System ===
            1. Register student
            2. Register Lecturer
            3. Set Course (Lecturer)
            4. List of course available (Public)
            5. Enroll in Course (Student)
            6. Check Lecturer Name (Public)
            7. Check Score (Student)
            8. Set Score (Lecturer)
            9. Exit
            """)
        choice = input("Enter choice (1-7): ")
        match choice:
            case "1":
                full_name = input("Enter full name: ")
                while not validat_input(full_name):
                    full_name = input("Enter full name: ")
                email = input("Enter email: ")
                while not validate_email(email):
                    email = input("Enter email: ")
                password = input("Enter password: ")
                while not len(password) > 6:
                    password = input("Enter password: ")
                student = Student(full_name, email, password)
                admin.register(student)
                print(f"Student registered successfully, matriculation number {student.get_matriculation_number}")

            case "2":
                full_name = input("Enter full name: ")
                while not validat_input(full_name):
                    full_name = input("Enter full name: ")
                email = input("Enter email: ")
                while not validate_email(email):
                    email = input("Enter email: ")
                password = input("Enter password: ")
                while not len(password) > 6:
                    password = input("Enter password: ")
                facilitator = Facilitator(full_name, email, password)
                admin.register(facilitator)
                print(f"Facilitator registered successfully, Staff id {facilitator.get_id()}")
            case "3":
                course_name = input("Enter course name: ")
                while not len(course_name) > 3:
                    course_name = input("Enter course name: ")
                course_code = input("Enter course code: ")
                while not valid_code(course_code):
                    course_code = input("Enter course code: ")
                try:
                  number = int(input("Enter your staff id: "))
                  facilitator_password = input("Enter your password: ")

                  facilitator = None
                  for user in admin.get_course_management_users():
                    if isinstance(user, Facilitator) and user.get_id() == number:
                        facilitator = user
                        break
                  if facilitator is None:
                      raise Exception("Facilitator not found")
                  if admin.verify_user(number, facilitator_password) is True:
                     admin.register_course(course_name, course_code, facilitator)
                     print(f"course {course_name} registered successfully")
                  else:
                      print("Access denied, staff does not exist, wrong Id or password.")
                except (Exception, TypeError) as e:
                    print(e)

            case "4":
                for course in admin.get_list_of_courses():
                    print(f"{course}")
            case "5":
                course_code = input("Enter course code: ")
                while not valid_code(course_code):
                     course_code = input("wrong course code format: ")
                try:
                   number = int(input("Enter your matriculation number: "))
                   student_password = input("Enter your password: ")
                   student = None
                   for user in admin.get_course_management_users():
                      if isinstance(user, Student) and user.get_matriculation_number == number:
                         student = user
                         break
                   if student is None:
                     raise Exception("Student not found")
                   if admin.verify_user(number, student_password) is True:
                      admin.enroll_student_to_course(student, course_code)
                      print(f"{student.get_full_name()},enrolled in {course_code} course")
                   else:
                       print("Access denied , Student does not exist, kind check your password")
                except (Exception, TypeError) as e:
                    print(e)
            case "6":
                course_code = input("Enter course code: ")
                while not valid_code(course_code):
                    course_code = input("wrong course code format: ")
                try:
                  result = admin.view_course_facilitator(course_code)
                  if result is None:
                      print("Course does not exist")
                  else:
                      print(f"facilitator is {result}")
                except  TypeError as e:
                    print(e)
            case "7":
                course_code = input("Enter course code: ")
                while not valid_code(course_code):
                    course_code = input("wrong course code format: ")
                try:
                   number = int(input("Enter your matriculation number: "))
                   student_password = input("Enter your password: ")
                   if admin.verify_user(number, student_password) is True:
                      score = admin.get_course_result(course_code, number)
                      print("Your score is:", score)
                   else:
                       print("Access denied, user does not exist, check your password.")
                except (Exception, TypeError) as e:
                    print(e)
            case "8":
                course_code = input("Enter course code: ")
                while not valid_code(course_code):
                    course_code = input("wrong course code format: ")
                try:
                   number = int(input("Enter student matriculation number: "))
                   facilitator_password = input("Enter your password: ")
                   id = int(input("Enter your Staff id: "))
                   score = int(input("Student your score: "))
                   while not (0 <= score <= 100):
                       score = input("Student your score: ")
                   if admin.verify_user(number, facilitator_password) is True:
                      admin.set_course_scores(course_code,id, score, number)
                      print("Score uploaded successfully")
                   else:
                       print("Access denied, user does not exist, check your password.")
                except (Exception, TypeError) as e:
                    print(e)
            case "9":
                   break
            case _:
                print("Invalid choice, please try again")













if __name__ == "__main__":
        main()