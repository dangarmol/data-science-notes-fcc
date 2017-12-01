import random
import os
import sys

print("Hello World!")

# Comment

'''
Multiline Comment
'''

name = "Dani"
print(name)

#Stuff in Python: Numbers, Strings, Lists, Tuples and Dictionaries (Hash)
'''
Operations:
+ - * / %
** (exp)
// (operation without remainder)
'''

print("5 / 2 =",5/2) #Why blank between = and result?

quote = "\"Always remember you are unique" #\" for quotes

multi_line_quote = ''' just
like everyone else"'''

print("%s %s %s" % ("I like this quote: ", quote, multi_line_quote))

print('\n' * 5) #This syntax works

print("I don't like ", end = "") #Avoid newlines
print("newlines")