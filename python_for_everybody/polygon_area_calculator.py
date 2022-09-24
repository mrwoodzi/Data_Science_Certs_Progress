class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
      
  def set_width(self, a):
    self.width = a
  
  def set_height(self, b):
    self.height = b

  def get_area(self):
    area = self.width * self.height
    return area
  
  def get_perimeter(self):
    perimeter = (2 * self.width + 2 * self.height)
    return perimeter
  
  def get_diagonal(self):
    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal
  
  def get_picture(self):
    pass # returns a formated string
    #return 
      
  def get_amount_inside(self):
    pass

  def __str__(self):
    str = f'Rectangle(width={self.width}, height={self.height})'
    return str


class Square(Rectangle):
  def __init__(self, l):
    self.width = l
    self.height = l
    
  def set_side(self, side):
    pass
    
  def __str__(self):
    str = f'Square(side={self.width})'
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
