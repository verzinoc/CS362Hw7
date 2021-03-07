import unittest
import FizzBuzz

class TestFizzBuxx(unittest.TestCase):
   def test_1(self):
      result = FizzBuzz.FizzBuzz()
      self.assertEqual(result, "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizzbuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 25 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 Fizzbuzz 46 47 Fizz 49 Buzz Fizz 52 53 Fizz Buzz 55 Fizz 58 59 FizzBuzz 61 62 Fizz 64 Buzz Fizz 67 68 Fizz Buzz 71 Fizz 73 74 Fizzbuzz 76 77 Fizz 79 Buzz Fizz 82 83 Fizz Buzz 85 Fizz 88 89 FizzBuzz 91 92 Fizz 94 Buzz Fizz 97 98 Fizz Buzz ")


if __name__ == "__main__":
   unittest.main(verbosity=2)
