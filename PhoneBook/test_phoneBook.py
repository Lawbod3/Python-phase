import unittest
from PhoneBook.phoneBook_method import phoneBook

class TestPhoneBook(unittest.TestCase):

      def test_phoneBook(self):
          contact = phoneBook()

      def test_is_empty(self):
          contact = phoneBook()
          self.assertTrue(contact.check_empty())

      def test_add_contact(self):
          contact = phoneBook()
          contact.add_contact("09023456788", "ole","you")
          self.assertFalse(contact.check_empty())

      def test_to_get_phoneBook_size(self):
          contact = phoneBook()
          self.assertEqual(0, contact.get_numbers_of_contact())
          contact.add_contact("09023456788", "ole","you")
          self.assertEqual(1, contact.get_numbers_of_contact())

      def test_to_remove_contact(self):
          contact = phoneBook()
          contact.add_contact("09023456788", "ole", "you")
          contact.remove_contact("09023456788")
          self.assertEqual(0, contact.get_numbers_of_contact())

      def test_to_get_contact_by_phoneNumber(self):
          contact = phoneBook()
          contact.add_contact("09023456788", "ole", "you")
          contact.set_email("09023456788","olabodelawal@gmail.com")
          answer = contact.get_contact_by_phone_number("09023456788")
          self.assertIn("firstname: ole", answer)
          self.assertIn("lastname: you", answer)
          self.assertIn("phone number : 09023456788", answer)
          self.assertIn("email: olabodelawal@gmail.com", answer)

      def test_to_find_contact_by_first_name(self):
          contact = phoneBook()
          contact.add_contact("09023456788", "ole", "you")
          answer = contact.find_by_first_name("ole")
          result = ["ole", "you", "09023456788"]
          result_two = []
          result_two.append(result)
          self.assertEqual(result_two, answer)

      def test_to_find_contact_by_last_name(self):
          contact = phoneBook()
          contact.add_contact("09023456788", "ole", "you")
          answer = contact.find_by_last_name("you")
          result = ["ole", "you", "09023456788"]
          result_two = []
          result_two.append(result)
          self.assertEqual(result_two, answer)















