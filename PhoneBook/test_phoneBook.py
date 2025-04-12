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
          self.assertEqual(1, contact.get_numbers_of_contact())

      def test_to_get_contact_by_phoneNumber(self):
          contact = phoneBook()
          contact.add_contact("09023456788", "ole", "you")
          contact.set_email("olabodelawal@gmail.com")
          result =  '''
          firstname: ole 
          lastname : you
          phone number: 09023456788
          email: olabodelawal@gmail.com
          '''
          self.assertEqual(result, contact.get_contact_by_phone_number("09023456788"))









