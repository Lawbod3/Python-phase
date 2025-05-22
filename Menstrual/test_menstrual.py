import unittest
from Menstrual.menstrual_method import menstrual_method
class TestMenstrualMethod(unittest.TestCase):
      def test_menstrual_method_period_day(self):
          cycle = menstrual_method(26,5,"2025-04-04")
          self.assertEqual("2025-04-30", cycle.get_period_day())

      def test_menstrual_method_get_ovulation(self):
          cycle = menstrual_method(26, 5, "2025-04-04")
          self.assertEqual("2025-05-14", cycle.get_ovulation())

      def test_menstrual_method_get_fertility_period(self):
          cycle = menstrual_method(26,5,"2025-04-04")
          self.assertEqual("2025-05-10 - 2025-05-14", cycle.get_fertility_period())

      def test_menstrual_method_get_flow_days(self):
          cycle = menstrual_method(26,5,"2025-04-04")
          self.assertEqual("2025-04-30 - 2025-05-05", cycle.get_flow_days())

      def test_menstrual_method_get_pre_ovulation(self):
          cycle = menstrual_method(26,5,"2025-04-04")
          self.assertEqual("2025-04-30 - 2025-05-13", cycle.get_pre_ovulation())

      def test_menstrual_method_get_post_ovulation(self):
          cycle = menstrual_method(26,5,"2025-04-04")
          self.assertEqual("2025-05-15 - 2025-05-25", cycle.get_post_ovulation())

      def test_menstrual_method_get_end_of_cycle(self):
          cycle = menstrual_method(26,5,"2025-04-04")
          self.assertEqual("2025-05-25", cycle.get_end_of_cycle())

      def test_menstrual_method_get_safe_day(self):
          cycle = menstrual_method(26,5,"2025-04-04")
          self.assertEqual("2025-04-30 - 2025-05-06", cycle.get_safe_day())

      def test_menstrual_method_get_post_ovulation_day(self):
          cycle = menstrual_method(26,5,"2025-04-04")
          self.assertEqual("2025-05-15 - 2025-05-25", cycle.get_post_ovulation())






if __name__ == '__main__':
    unittest.main()