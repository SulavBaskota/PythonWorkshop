"""
Q13. Write a definition for a class named Circle with attributes center and radius ,
where center is a Point object (tuple) and radius is a number.
Instantiate a Circle object that represents a circle with its center at ( 150, 100 ) and radius 75.
"""


class Circle:

    def __init__(self, center,radius):
        self.center = center
        self.radius = radius

x = int(input("Enter x coordinate of center: "))
y = int(input("Enter y coordinate of center: "))
r = int(input("Enter radius: "))
circle_1 = Circle((x,y),r)
print(circle_1.center)
print(circle_1.radius)
