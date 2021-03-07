def FizzBuzz(option):

   counter = ""
   count = 0
   for x in range(100):
      temp = x + 1
      count = count + 1
      if ((temp) % 3) == 0 and ((temp) % 5) == 0:
	 counter = counter + "FizzBuzz "
      elif ((x+1)%3) == 0:
	 counter = counter + "Fizz "
      elif ((x+1)%5) == 0:
	 counter = counter + "Buzz "
      else:
	 counter = counter + str(temp) + " "

   if option == 2:
      return count
   else:
      return counter

