class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
      
  def set_width(self, a):
    pass
  
  def set_height(self, b):
    pass
  
  def get_area(self):
    pass # (width * height)
    #return self.area
  
  def get_perimeter(self):
    pass # (2 * width + 2 * height)
    #return self.perimeter
  
  def get_diagonal(self):
    pass #  ((width ** 2 + height ** 2) ** .5)
    #return self.diagonal
  
  def get_picture(self):
    pass # returns a formated string
    #return 
      
  def get_amount_inside(self):
    pass

  def __str__(self):
    pass # str format -> Rectangle(width=5, height=10)
    str = f'Hey Cutie!'
    return str

class Square(Rectangle):
  def __init__(self, height):
    self.height = height
    
  def set_width(self, height):
    pass

  def set_heigth(self, height):
    pass

  def set_side(self, side):
    pass
    
  def __str__(self): # do I put square or self here?
    pass # str format -> Square(side=9)
    str = f'Hey Baby'
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
