import unittest
import LeapYear

class TestLeapYear(unittest.TestCase):
   def test_1(self):
      result = LeapYear.LeapYear(2004)
      self.assertEqual(result, 1)

   def test_2(self):
      result = LeapYear.LeapYear(300)
      self.assertEqual(result, 0)

   def test_3(self):
      result = LeapYear.LeapYear(400)
      self.assertEqual(result, 1)

if __name__ == "__main__":
   unittest.main(verbosity=2)
