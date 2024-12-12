# Section 2, Exercise 2b: From following the solution.
# This is a general reference standard for opening files in python, using a "with open" format.  The
#   function also shows a general process for reading configuration files, with key : value pairs.  Finally,
#   the function is changed to allow for receiving and reading multiple files.
# Lines 9, 10 and 19 form the initial shell of the function.
# Lines 13 and 14 are the general form of the with open file process.
# Replace filename with *args to accept any number of files, then add a for ... args line.

def get_config(*args): # filename
    output = {}

    for filename in args:
        with open(filename) as f:
            for one_line in f:
                if ':' in one_line:
                    key, value = one_line.split(':')
                    output[key.strip()] = value.strip()

    return output

# get_config('/Users/rrdoue/Documents/applications/python/LernerPython/files/exercise-files/config1.txt',
#            '/Users/rrdoue/Documents/applications/python/LernerPython/files/exercise-files/config2.txt'))

