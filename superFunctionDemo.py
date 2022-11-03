# super() = Function used to give access to the method of a parent class.
# returns a temp object of a parent class when used.

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square(Rectangle):

    def __init__(self, length, width):
        super().__init__(length,width)
        #self.length = length #Notice how we have to reuse all this code...not optimal.
        #self.width = width

    def area(self):
        return self.length * self.width


class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height #you still need to keep the height since it isn't defined in rectangle
        # self.length = length
        # self.width = width
    def volume(self):
        return self.length * self.width * self.height

square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())