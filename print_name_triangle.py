#! /usr/bin/env python3

# Section 4, Exercise 4: Name Triangle
# Ask the user to enter their name.  Print their name as a triangle.  
#   For example, the first letter, another line withtwo letters, another line 
#   with three letters, until you've printed their full name.  This has been 
#   called a name triangle.

debug = None 
s = ' '

user_name = input('Please enter your name: ').strip()

if debug:
    print(f'\nName Length: {len(user_name)} character(s)\n')

# My original version, with Reuven's improvements, which I like better
for idx, one_letter in enumerate(user_name, start=1):

    if debug:
        print(f'{user_name[:idx]}{s * (len(user_name) + 2 - idx)}{idx-1}')
    else:
        print(f'{user_name[:idx]}')

# Reuven used a range(len(user_name)) instead of an enumerate and also left off 
#   the initial 0, just using [:idx+1]
# for idx in range(len(user_name)):
#     print(user_name[:idx+1])

