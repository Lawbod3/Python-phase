import unittest
from collection.creditCard import convert_to_array, validate_length, sum_array_last, sum_array_second_to_last, \
    get_card_type


class TestCreditCard(unittest.TestCase):
      def test_convert_to_array_method(self):
          input_str = "123456789"
          expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
          actual = convert_to_array(input_str)
          self.assertEqual(expected, actual)

      def test_to_validate_input_length(self):
          input_str = "123456789"
          self.assertFalse(validate_length(input_str))

      def test_method_sum_array_from_last_index(self):
          input = [1, 2, 1, 4, 1, 6, 1, 8, 1]
          expected = 5
          self.assertEqual(expected, sum_array_last(input))


      def test_method_sum_array_from_second_to_last_index(self):
          input = [1, 2, 1, 2, 1, 2, 1, 2, 1]
          expected = 16
          self.assertEqual(expected, sum_array_second_to_last(input))

      def test_method_get_card_type(self):
          input_str = "3723456789"
          expected = "Amex"
          self.assertEqual(expected, get_card_type(input_str))





if __name__ == '__main__':
    unittest.main()
