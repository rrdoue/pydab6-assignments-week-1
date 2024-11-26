#! /usr/bin/env python3

# Section 3, Exercise 3: Pig Latin Translator

# Requirements courtesy of Norman Eliaser

# Pig Latin
# (1) If the first letter is a vowel, add way
# (2) If the first letter is not a vowel, move the first letter to the end of the word, and add "ay"
# Ask the user to enter one English word, without punctuation or capital letters
#   and print the translation in Pig Latin
# Tested with the following: away, orca, supercalifragilisticexpialidocious, wayfair

debug = None # for future debugging

response = input('Please give us a word in English without capital letters or puncuation: ')

if response[0] in 'aeiou':
    pig_latin_translation = response + 'way'
else:
    pig_latin_translation = response[1:] + response[0] + 'ay'

print('The word \'' + response + '\' in Pig Latin is \'' + pig_latin_translation + '\'.')

