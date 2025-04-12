import unittest
from PhoneBook.phoneBook_method import phoneBook

class TestPhoneBook(unittest.TestCase):

      def test_phoneBook(self):
          contact = phoneBook()

      def test_phoneBook_add_contact(self):
          contact = phoneBook()
          contact.add_contact("", "<EMAIL>","")



