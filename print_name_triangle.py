#! /usr/bin/env python3

# Section 4, Exercise 4b: Name Triangle 

# Ask the user to enter their name. 
# Print their name as a triangle. 
# For example, the first letter on one line, the next line with two letters,  
#   the next line with three letters, until you've printed their entire name. 
# This has been called a name triangle.

user_name = input('Please enter your name: ').strip()

# Reuven used a range(len(user_name)) instead of an enumerate. 
# He also left off the initial 0, just using [:index+1]
# for index, one_letter in enumerate(user_name):
#     print(user_name[:index+1])

for idx in range(len(user_name)):
    print(user_name[:idx+1])

