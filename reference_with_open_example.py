#! /usr/bin/env python3

# Section 1, Exercise 2a: From following the solution.
# This is a general reference standard for opening files in python, using a "with open" format.
# Given a filename, count the characters in a file, then return the output as a dictionary.  Use a
#   function for this exercise.
# Lines 8, 9 and 20 form the initial shell of the function.
# Lines 12 and 13 are the general form of the with open file process.

def count_characters(filename):
    output = {}

#    for one_line in open(filename): # change this to use with
    with open filename as f:
        for one_line in f:
            for one_character in one_line:
                if one_character in output:
                    output[one_character] += 1
                else:
                    output[one_character] = 1

    return output

# count_characters('/etc/passwd')
