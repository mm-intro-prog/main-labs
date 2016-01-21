"""
IMPORTANT STUFF:

This file is basic 'skeleton code' for the exercises that you will be asked to
complete in this lab.  You must put your answers in the correct section that is
designated in the comments.  Things should be in order so just scroll down the
page as you go through the lab exercises.

There is no test code in this lab, so you will always be running the whole file.
"""


your_name = ""

#############################################################
# Exercise 1
#
# Write a class to define a circle.
# The circle has a single property called radius.
# The circle has one behavior to calculate the area.
#   - The area is calculated as follows:
#        area = 3.14 * radius * radius
#
# Use encapsulation to hide the property, so you need to add
# a method to get and set the radius.
############################################################

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius



#############################################################
# Exercise 2
#
# Use your circle class to make two circle objects:
#  - one with a radius of 4
#  - the other with a radius of 6
# Print the radius and area of each circle.
############################################################

circle4 = Circle()
circle.rad



#############################################################
# Exercise 3
#
# Make a cylinder class that inherits from your cirle.
# It should add a new property called height.
# The cylinder has one new behavior to calculate the base_area.
#   - The area is calculated as follows:
#        area = 3.14 * radius * radius
############################################################
