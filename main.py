from turtle import *
import math
#малювашка
#коло
ht()
speed(0)
color("red")
speed(0.0002)
width(3)
circle(30)
up()
right(-90)
forward(30)
right(90)
forward(40)
down()
forward(10)
right(90)
write("circle")
right(-90)
forward(30)
up()
right(180)
forward(78)
right(-90)
forward(70)

# Прямокутник
right(90)
forward(30)
pendown()
color("blue")
right(-90)

forward(40)
right(-90)
forward(60)
right(-90)
forward(40)
right(-90)
forward(60)
right(-90)

penup()
right(90)
forward(50)
right(-90)
forward(20)
write("rectangle",)
pendown()
right(-90)
forward(35)
penup()
right(90)
forward(70)
right(-90)
forward(25)

# Трикутник
pendown()
color("green")
right(40)
forward(50)
right(141)
forward(40)
right(90)
forward(30)
penup()
right(90)
forward(50)
right(90)
forward(15)
write("triangle",)
pendown()
right(-90)
forward(35)
penup()
right(90)
forward(50)
right(90)
forward(90)
right(-90)

# Квадрат
pendown()
color("purple")
right(-90)
for _ in range(4):
    forward(50)
    right(90)

penup()
forward(25)
right(180)
forward(60)
left(90)
forward(30)
left(90)
write("square",)
pendown()
forward(30)



class Shape:
    def __init__(self, color=0):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):

        self.__color = color

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def describe(self):
        return f"This shape has color {self.__color}"

class Circle(Shape):
        def __init__(self, radius=3, color="red", center=(0, 0)):
            super().__init__(color)
            self.__radius = radius
            self.__center = center


        def get_radius(self):
            return self.__radius

        def set_radius(self, radius):
            self.__radius = radius

        def area(self):
            return math.pi * self.__radius ** 2

        def perimeter(self):
            return 2 * math.pi * self.__radius

        def diameter(self):
            return 2 * self.__radius

        def move_center(self, x, y):
            self.__center = (x, y)

        def describe(self):
            return f"Circle with radius: {self.__radius}, center: {self.__center}, color: {self.get_color()}."

class Rectangle(Shape):
    def __init__(self, width, height, color="purple",  position=(0, 0)):
        super().__init__(color)
        self.__width = width
        self.__height = height
        self.__position = position

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def is_square(self):
        return self.__width == self.__height

    def move(self, dx, dy):
        x, y = self.__position
        self.__position = (x + dx, y + dy)

    def describe(self):
        return f"Rectangle have width: {self.__width}, height: {self.__height}, position: {self.__position}, color: {self.get_color()}."


class Triangle(Shape):
    def __init__(self, side1, side2, side3, triangle_type="scalene", color="green"):
        super().__init__(color)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        self.__type = triangle_type

    def perimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def triangle_type(self):
        return self.__type

    def scale(self, factor):
        self.__side1 *= factor
        self.__side2 *= factor
        self.__side3 *= factor

    def describe(self):
        return f"{self.__type.capitalize()} triangle with sides {self.__side1}, {self.__side2}, {self.__side3}, color {self.get_color()}."


class Square(Rectangle):
    def __init__(self, side1, side2, color="Black", position=(0, 0),corners=4):
        super().__init__(width=side1, height=side2, color=color, position=position)
        self.__side1 = side1
        self.__side2 = side2
        self.__corners = corners

    def get_sides(self):
        return (self.__side1, self.__side2)

    def is_square(self):
        return self.__side1 == self.__side2

    def describe(self):
        shape_type = "Square" if self.is_square() else "Rectangle-like"
        return f"{shape_type} with sides {self.__side1} and {self.__side2} at {self._Rectangle__position}, corners: {self.__corners}, color: {self.get_color()}.\n"


def TotalArea(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

circle = Circle(radius=3, center=(1, 3),color="red",)
rectangle = Rectangle(width=6, height=4, color="blue", position=(0, 0))
triangle = Triangle(side1=3, side2=4, side3=5, triangle_type="right", color="green")
square = Square(side1=5, side2=5 , position=(0, 1), corners=4, color="purple" )


print(circle.describe())
print(f"Circle area: {circle.area():.0f}, perimeter: {circle.perimeter():.0f}, diameter: {circle.diameter()}\n")

print(rectangle.describe())
print(f"Rectangle area: {rectangle.area()}, perimeter: {rectangle.perimeter()}, is square: {rectangle.is_square()}\n")

print(triangle.describe())
print(f"Triangle area: {triangle.area():.0f}, perimeter: {triangle.perimeter()}, type: {triangle.triangle_type()}\n")

print(square.describe())

shapes = [circle, rectangle, triangle]

print(f"Total area of all shapes: {TotalArea(shapes):.0f}\n")

print(f"Circle > Rectangle: {circle > rectangle}")
print(f"Triangle < Square: {triangle < rectangle}")

done()

