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
   chart_builder = ""



   return chart_builder