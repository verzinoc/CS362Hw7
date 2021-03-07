import unittest
import LeapYear

class TestLeapYear(unittest.TestCase):
   def test_1(self):
      result = LeapYear.LeapYear(2004)
      self.assertEqual(result, 1)

if __name__ == "__main__":
   unittest.main(verbosity=2)
