import math

class Category:

   def __init__(self, name):
      self.name = name
      self.ledger = list()  # This needs to be created here, NOT as a class variable. Otherwise it would be shared by all instances!
      self.balance = 0
   

   def deposit(self, amount, description = ""):
      self.balance += amount
      self.ledger.append({"amount": amount, "description": description})
      

   def withdraw(self, amount, description = ""):
      if self.check_funds(amount):
         self.ledger.append({"amount": (amount * -1), "description": description})
         self.balance -= amount
         return True
      else:
         return False
   
   
   def get_balance(self):
      return self.balance

   
   def get_name(self):
      return self.name


   def get_ledger(self):
      return self.ledger


   def transfer(self, amount, new_category):
      if not self.withdraw(amount, "Transfer to " + new_category.get_name()):
         return False
      else:
         new_category.deposit(amount, "Transfer from " + self.name)
         return True


   def check_funds(self, amount):
      return self.balance >= amount


   def __str__(self):
      string_builder = self.name.center(30, '*') + "\n"

      for transaction in self.ledger:
         description = transaction["description"][:23].ljust(23)
         amount = ("%.2f" % transaction["amount"])[:7].rjust(7) + "\n"
         string_builder += description
         string_builder += amount

      string_builder += "Total: %.2f" % self.balance
      
      return string_builder


def create_spend_chart(categories):
   chart_builder = "Percentage spent by category\n"

   percentages = calculate_rounded_percentage(categories)
   category_names = list(percentages.keys())

   for x in reversed(range(0, 101, 10)):
      chart_builder += str(x).rjust(3) + "|"
      for name in category_names:
         if percentages[name] >= x:
            chart_builder += " o "
         else:
            chart_builder += "   "
      chart_builder += " \n"

   chart_builder += " " * 4 + "-" * ((len(category_names) * 3) + 1) + "\n"

   max_length = longest_word(category_names)

   for height in range(max_length):
      chart_builder += " " * 4
      for name in category_names:
         if len(name) > height:
            chart_builder += " " + name[height] + " "
         else:
            chart_builder += " " * 3
      chart_builder += " \n"

   return chart_builder


def longest_word(category_names):
   max = 0

   for word in category_names:
      if len(word) > max:
         max = len(word)

   return max


# Returns the equivalent percentages in a dictionary as an integer multiple of 10 for each category
def calculate_rounded_percentage(categories):
   percentages = dict()
   category_totals = dict()
   total_spent = 0

   for category in categories:
      for transaction in category.get_ledger():
         if transaction["amount"] < 0:
            total_spent -= transaction["amount"]
            category_totals[category.get_name()] = category_totals.get(category.get_name(), 0) - transaction["amount"]

   for category_name in category_totals.keys():
      percentages[category_name] = math.trunc((category_totals[category_name] / total_spent) * 10) * 10

   return percentages
