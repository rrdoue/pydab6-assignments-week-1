#! /usr/bin/env python3

# Section 4, Exercise 4a
# Ask the user to enter an integer or number, then ask for their name. 
# Using the integer, print their name that number of (integer) times. 

integer_response = input('Please enter a number, say, from 3 to 7: ')

name = input('Please enter your name: ')
print(f"\nWe're printing your name {integer_response} times:\n")

for one_number in range(int(integer_response)):
    print(name)

