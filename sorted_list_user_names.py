#! /usr/bin/env python3

# Incorporating some of Reuven's ideas, like his how to make a tuple lesson.

# Section 6, Exercise 7: People's Names, First and Last Name List

# Ask the user to enter a first and last name pair until the user enters an 
#   empty string.  Prompt the user if the names are not separated by a space.
# Store the names in a list of tuples as last name, first name.
# When the user stops entering names, print the list sorted by last name.

debug = None

user_list = [ ]

while True:
    user_name = input('Please enter a name consisting of a first and last name: ').strip()

    if not user_name:
        break
    if ' ' not in user_name: # Reuven ran it like this
        print(f'The user name, {user_name}, does not appear to follow the requested format, please try again.')
        continue
    if user_name.count(' ') > 1: # Reuven added this for fun
        print(f'You entered too many spaces, does not appear to follow the requested format, please try again.')
    else:
        first, last = user_name.split()
        if debug:
            tmp_tuple = (last, first) # first version omitted parentheses
            print(f'Adding to list: {tmp_tuple}')
        user_list.append( (last, first) ) # Reuven demonstrated this tuple format
        if debug:
            print(f'User list: {user_list}\n')

print(f'\nList of Users:')
for last, first in sorted(user_list):
    print(f'{last}, {first}')

#Grace Slick, Stevie Nicks, Cristine McVie, Barbra Streisand, Ella Fitzgerald, Dionne Warwick, Whitney Houston, Donna Summer, Annie Lennox

