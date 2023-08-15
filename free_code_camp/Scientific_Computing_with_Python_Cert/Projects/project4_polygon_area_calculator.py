class Rectangle:
    def __init__(self, width, height):
        self.width = width  # instance attribute
        self.height = height  # instance attribute

    def set_width(self, a):  # instance method
        self.width = a

    def set_height(self, b):  # instance method
        self.height = b

    def get_area(self):  # instance attribute
        area = self.width * self.height
        return area

    def get_perimeter(self):  # Instance Attribute Outside of Init
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):  # Instance Attribute Outside of Init
        diagonal = (self.width**2 + self.height**2) ** 0.5
        return diagonal

    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            too_big = "Too big for picture."
            get_picture = too_big
        else:
            star = "*" * self.width + "\n"
            sq_rect = star * self.height
            get_picture = sq_rect
        return get_picture

    # get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of
    # times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle
    # with a width of 4 and a height of 8 could fit in two squares with sides of 4.
    def get_amount_inside(self, shape):  # Instance Attribute Outside of Init
        x = self.height * self.width
        y = shape.height * shape.width
        amount = int(x / y)
        if amount >= 1:
            amount_inside = amount
        else:
            amount_inside = 0
        return amount_inside

    def __str__(self):
        str = f"Rectangle(width={self.width}, height={self.height})"
        return str


class Square(Rectangle):
    def __init__(self, l):
        self.width = l
        self.height = l

    def set_side(self, side):
        self.width = side
        self.height = side

    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            too_big = "Too big for picture."
            get_picture = too_big
        else:
            star = "*" * self.width + "\n"
            sq_rect = star * self.height
            get_picture = sq_rect
        return get_picture

    def __str__(self):
        str = f"Square(side={self.width})"
        return str


Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
