#! /usr/bin/env python3

# Section 5, Exercise 6: Pig Latin Translator for a Sentence

# Pig Latin (courtesy of Norman Eliaser)
# (1) If the first letter is a vowel, add "way" to the end of the word
# (2) If the first letter is not a vowel, move the first letter to the end of 
#     the word, and add "ay"
# Ask the user to enter a sentence, without punctuation or capital letters
#   and print the translation in Pig Latin as a sentence
# Tested with the following: " this is a test sentence "

debug = None # for future debugging

word_list = [ ]
new_sentence = ''
pig_latin_sentence = ''

sentence = input('Please enter a sentence in English without capital letters or puncuation: ').strip()

word_list = sentence.split()
english_sentence = sentence

for index, one_word in enumerate(word_list):
    if one_word[0] in 'aeiou':
        replacement_word = one_word + 'way'
        word_list[index] = replacement_word
    else:
        replacement_word = one_word[1:] + one_word[0] + 'ay'
        word_list[index] = replacement_word

pig_latin_sentence = ' '.join(word_list)

print(f'English sentence: {english_sentence}')
print(f'Pig Latin sentence: {pig_latin_sentence}')

