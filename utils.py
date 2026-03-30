import greet
from area import circle,rectangle,square,triangle
def circle(r):
    print("This is the circle function in utils.py")
print("Area of circle with radius 5 is",circle(5))
greet.gm("Archi")
greet.ge("arch")
greet.gn("Archana")
print("area of circle of radius 5:",circle(5))
print("area of rec of length 4 and breadth 6:",rectangle(4,6))
print("area of square of side 3:",square(3))
print("area of triangle of base 4 and height 5:",triangle(4,5))