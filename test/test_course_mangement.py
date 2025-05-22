import unittest
from Users.Student import Student
from Users.facilitator import  Facilitator
from course_management import CourseManagement


class MyTestCase(unittest.TestCase):



    def setUp(self):
        self.myself = Student("lawal olabode", "olabodelawal3@gmail.com", "<PASSWORD>")
        self.teacher = Facilitator("chibuzor Ayinla", "chibuzor Ayinla@gmail.com", "<PASSWORD>" )
        self.admin = CourseManagement()
        self.admin.register(self.myself)
        self.admin.register(self.teacher)
        self.admin.register_course("python", "python101", self.teacher)

    def test_Course_management_can_register_users(self):
        self.assertEqual(self.myself, self.admin.register(self.myself))
    def test_facilitator_can_create_a_course(self):
        self.assertEqual(1, self.admin.course_available())
    def test_student_can_enroll_a_course(self):
        self.admin.enroll_student_to_course(self.myself, "python101")
        self.assertEqual(1, self.myself.get_number_of_courses_offered())
    def test_student_can_view_course_facilitator(self):
        self.assertEqual("chibuzor Ayinla", self.admin.view_course_facilitator("python101"))
    def test_facilitator_can_set_course_scores(self):
        self.assertEqual(1001, self.myself.get_matriculation_number)
        self.admin.enroll_student_to_course(self.myself, "python101")
        self.admin.set_course_scores("python101", 1,95, 1001)
        self.assertEqual(95, self.admin.get_course_result("python101", 1001))

    def test_student_can_be_verified(self):
        self.assertTrue(self.admin.verify_user(1001,"<PASSWORD>" ))
        self.assertTrue(self.admin.verify_user(1, "<PASSWORD>"))










if __name__ == '__main__':
    unittest.main()
