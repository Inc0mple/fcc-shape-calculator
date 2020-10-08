import math

class Rectangle:
    def __init__(self,width,height):
        super().__init__()
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self,width):
        self.width = width
    
    def set_height(self,height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        output = ""
        if (self.width > 50 or self.height > 50):
            return "Too big for picture."
        for x in range(self.height):
            output += "*"*self.width
            output += "\n"
        return output

    def get_amount_inside(self, shape):
        return math.floor(self.height/shape.height) * math.floor(self.width/shape.width)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)
        self.side = side
        self.width = side
        self.height = side

    def __repr__(self):
        return f"Square(side={self.side})"

    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side

    def set_width(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

    def set_height(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

