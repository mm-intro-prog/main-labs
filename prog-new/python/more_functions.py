"""
This is the second HW lab for python.
"""

# Enter your full name here.
your_name = "Silly Student"


print( "HW 9: " + your_name)

####################################################
# Exercise 1:
#  Define a single function that uses _two_ for loops
#  to count from 0 up to some number and then down
#  from that same number to 0.
####################################################
print("\nExercise 1 - no output")



####################################################
# Exercise 2:
#  Call the function that you made in excersise 1
#  to count up to 5 and back down.
####################################################
print("\nExercise 2")


####################################################
# Exercise 3:
#  The code below will ask the user for the number
#  to count to.  That value is then converted from
#  a string to an integer.
#
#  Call the function that you made in excersise 1
#  to count up to the number entered and back down.
####################################################
print ("\nExercise 3")
str_number = raw_input("Enter the number to count to: ")
number = int(str_number)




####################################################
# Exercise 4:  Even number?
#  Define a function that will return true if a
#  number is even and false otherwise. (Note - a
#  number is even if there is no remainder when the
#  number is divided by 2 - use modulus operator.)
####################################################
print ("\nExercise 4 - no output")



####################################################
# Exercise 5:
#  Use the function that you made in exercise 4 to
#  write a short script that asks the user to enter
#  a number then tells them (prints a message) if
#  the number is even or odd.
####################################################
print ("\nExercise 5")


####################################################
# Exercise 6:  Guessing game
#  Write the number guessing game in python.
#  The code below will pick a random number from
#  1 - 100.  Ask the user to guess a number until
#  they guess correctly.  If the guess is wrong,
#  print messages to tell if the players guess is
#  too high or too low.
#
#  Define functions to help make the code easier to
#  read, write and understand.
####################################################
print ("\nExercise 6 - Number Guessing Game")
import random
secret_number = random.randint( 1, 100 )




####################################################
print("\nEnd of HW 9")
