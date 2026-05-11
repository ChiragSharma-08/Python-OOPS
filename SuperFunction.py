#super() = Function used in a child class to call method from a parent class (superclass)
#          Allows you to extend the functionality of the inherited method

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    def describe(self):
        return print(f"It is {self.color} and {'filled'if self.is_filled else 'not filled' }")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is a {self.color} circle of area {3.14*self.radius*self.radius}cmsq")

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        super().describe()
        print(f"It is a {self.color} square of area {self.width*self.width}cmsq")

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle(color="red", is_filled=True, radius=6)
square = Square(color="green", is_filled=False, width=2)
triangle = Triangle(color="blue", is_filled=False, width=3, height=4)

print(circle.is_filled)
print(f"{circle.radius}cm")

circle.describe();print("")
square.describe()