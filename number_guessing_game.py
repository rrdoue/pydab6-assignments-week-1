#! /usr/bin/env python3

# Note: To run the most easily from a command line, use the syntax python3 <file_name>
# Or ensure the file is executable, then include a `./` before the file name.  
# For example, 
# chmod +x <file_name>
# or chmod u+x <file_name>
# Then,
# ./<file_name>

# Section 1, Exercise 2: number guessing game

import random

response = ''

target_number = random.randint(1, 100)

response = input('Please guess a number between 1 and 100: ')

print('You guessed \'' + response + '\'.')

if response.isnumeric():
    user_input = int(response)
    print('The random number is \'' + str(target_number) + '\'.')
    if user_input == target_number:
        print('Congratulations, you got the number correct!')
    elif user_input < target_number:
        print('Sorry, you selected a number that is less than our number. Thanks for playing the game.')
    elif user_input > target_number:
        print('Sorry, you selected a number that is higher than our number. Thanks for playing the game.')
else:
    print('That input does not appear to be a valid number, sorry but you only get one try.')

