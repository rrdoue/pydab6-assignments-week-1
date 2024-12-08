#! /usr/bin/env python3

# Section 8, Exercise 11: Fun with Spelling and Guessing Words

# Define a word that contains seven different letters, or is a collection of 
#   seven different letters.
# Ask the user to enter a string, and if it is an empty string, exit.  If the 
#   string contains only letters from the seven defined letters, congratulate  
#   them.  If not, then say something else.
# I interpreted the requirements as the user string had to contain all of the
#   letters in our list, but Reuven meant just what I said above, that their
#   word contains only our letters, but not necessarily all of them.
# A sample successful word is "perjure" — it uses only letters from our list.
# Retried in this version after seeing the approved solution. 

debug = None

comparison_set = { 'j', 'u', 'p', 'y', 't', 'e', 'r' }

while True:
    word = input('Please enter a word to compare to our test word: ').strip().lower()

    their_set = set(word)

    if not word:
        break
    
    elif their_set <= comparison_set:
        print(f'\nHooray (yay), you got it!')
    else:
        missing_set = their_set - comparison_set
        print(f'\nSorry (boo), you didn\'t guess correctly.  You used the following '
              f'letters that are not in our set: {missing_set}')

print('\nThanks for playing the game!')
