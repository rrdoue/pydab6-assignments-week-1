#! /usr/bin/env python3

# Section 8, Exercise 11: Fun with Spelling and Guessing Words

# Define a word that contains seven different letters, or is a collection of 
#   seven different letters.
# Ask the user to enter a string, and if it is an empty string, exit.  If the 
#   string contains only letters from the seven defined letters, congratulate  
#   them.  If not, then say something else. 

debug = None

comparison_set = { 'j', 'u', 'p', 'y', 't', 'e', 'r' }

while True:
    word = input('Please enter a word to compare to our test word: ').strip().lower()

    if not word:
        break
    
    else:
        their_set = set(word)
        if not comparison_set.symmetric_difference(their_set):
            print(f'Hooray (yay), you got it!')
        else:
            missing_set = comparison_set - their_set
            print(f'Sorry (boo), you didn\'t guess correctly.  You were missing the following letters: {missing_set}')

print('\nThanks for playing the game.')

