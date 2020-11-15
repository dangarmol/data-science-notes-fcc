import math


class Rectangle:
   def __init__(self, width, height):
      self.width = width
      self.height = height


   def set_width(self, width):
      self.width = width


   def set_height(self, height):
      self.height = height


   def get_width(self):
      return self.width


   def get_height(self):
      return self.height


   def get_area(self):
      return self.width * self.height


   def get_perimeter(self):
      return 2 * self.width + 2 * self.height


   def get_diagonal(self):
      return (self.width ** 2 + self.height ** 2) ** .5


   def get_picture(self):
      if self.width > 50 or self.height > 50:
         return "Too big for picture."

      picture_builder = ""

      for i in range(self.height):
         picture_builder += ("*" * self.width) + "\n"

      return picture_builder


   def get_amount_inside(self, shape):
      horizontal_fit = math.trunc(self.width / shape.get_width())
      vertical_fit = math.trunc(self.height / shape.get_height())
      return horizontal_fit * vertical_fit


   def __str__(self):
      return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"



class Square(Rectangle):
   def __init__(self, side_length):
      super().__init__(side_length, side_length)


   def set_side(self, side_length):
      super().set_height(side_length)
      super().set_width(side_length)


   def set_width(self, width):
      self.set_side(width)


   def set_height(self, height):
      self.set_side(height)


   def __str__(self):
      return "Square(side=" + str(self.height) + ")"
