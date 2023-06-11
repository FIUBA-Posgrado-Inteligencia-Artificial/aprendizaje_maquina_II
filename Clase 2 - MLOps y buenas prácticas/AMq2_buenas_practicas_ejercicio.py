import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        dx = abs(self.x - other_point.x)
        dy = abs(self.y - other_point.y)
        return math.sqrt(dx ** 2 + dy ** 2)

class Circle:
    def __init__(self, center, radius):
      self.c = center
      self.r = radius

    def area(self):
        return math.pi * self.r ** 2

if __name__ == "__main__":
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    distance = p1.distance(p2)

    circle = Circle(Point(0, 0), 5)
    area = circle.area()

    print("The distance between the points is:", distance,"and the area of the circle is:", area,"\n Thanks for use this program!")