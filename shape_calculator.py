class Rectangle:
  """Creates rectangles which can be displayed
  as strings.
"""

  def __init__(self, width,height):
    """Attributes
       ----------
    width : int, the rectangle's width
    height : int, the rectangle's height
    """
    self.width = width
    self.height = height

  def set_width(self,width) :
    self.width = width

  def set_height(self,height) :
    self.height = height

  def get_area(self) :
    area = self.width * self.height
    return area

  def get_perimeter(self) :
    perimeter = 2 * self.width + 2 * self.height
    return perimeter

  def get_diagonal(self) :
    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal
    
  def get_picture(self) :
    if self.width > 50 or self.height > 50:
      picture = "Too big for picture."
    else:
      picture = ""
      w = "*" * self.width
      for i in range(self.height):
        picture+= w
        if i < self.height:
          picture+= "\n"
          
    return picture

  def get_amount_inside(self,shape):
    a1 = self.get_area()
    a2 = shape.get_area()
    amount = a1 //a2
    return amount
    
  def __str__(self):
    strRect = f"Rectangle(width={self.width}, height={self.height})"
    return strRect


class Square(Rectangle):
  """A child class of the Rectangle class
  that creates squares."""

  def __init__(self,side):
    """Attributes
       ----------
    width : int, the side
    height : int, the side
    """
    self.width = side
    self.height = side

  def set_side(self,side) :
    self.width = side
    self.height = side

  def set_width(self,width) :
    """Overrides the Rectangle class set_width method."""
    self.width = width
    self.height = width

  def set_height(self,height) :
    """Overrides the Rectangle class set_height method."""
    self.height = height
    self.width = height

  def __str__(self) :
    """Returns the Square object as a string."""
    strSqu = f"Square(side={self.width})"
    return strSqu
