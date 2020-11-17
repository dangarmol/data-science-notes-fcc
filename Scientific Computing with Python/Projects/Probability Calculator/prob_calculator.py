import random
import copy
# Consider using the modules imported above.

class Hat:
   def __init__(self, **kwargs):
      self.contents = list()
      self.initial_count = 0
      for key, value in kwargs.items():
         for i in range(value):
            self.initial_count += 1
            self.contents.append(key)


   def draw(self, num):
      chosen = list()

      try:
         for i in range(num):
            index = random.randint(0, len(self.contents) - 1) if len(self.contents) - 1 > 0 else 0
            chosen.append(self.contents[index])
            self.contents.pop(index)
      except IndexError:
         return chosen
      
      return chosen



# This module has some poor data structure choices, but they were required by the instructions.
# Otherwise, the tests might not pass.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
   successes = 0
   
   for i in range(num_experiments):
      expected = expected_balls.copy()
      drawn = copy.deepcopy(hat).draw(num_balls_drawn)
      for ball in drawn:
         if ball in expected.keys():
            expected[ball] -= 1
            if expected[ball] == 0:
               del expected[ball]
         if not bool(expected):  # If the dictionary is empty it will evaluate to false
            successes += 1
            break

   return successes / num_experiments