#! /usr/bin/env python3

# Section 4, Exercise 4b: Name Triangle 

# Ask the user to enter their name. 
# Print their name as a triangle. 
# For example, the first letter on one line, the next line with two letters,  
#   the next line with three letters, until you've printed their entire name. 
# This has been called a name triangle.

user_name = input('Please enter your name: ')

for index, one_letter in enumerate(user_name):
    print(user_name[0:(index + 1)])

