#! /usr/bin/env python3

# python-functions, Section 4, Exercise 19b: Define a function that takes one mandatory 
#   argument, the name of an output file, any number of additional input file arguments, 
#   and an optional separator argument that defaults to an empty string.  The function 
#   should read all of the lines in each input file and write them to the named output 
#   file, adding theseparator in between the contents of each input file. 
#   The test cell uses files in the current executable file location to avoid having to 
#   provide a full path to the input files. 

def process_files(output_file, *input_files, separator=''):

    import os

    debug = None
    
    output_file_destination = '/Users/rrdoue/Documents/applications/python/LernerPython/files/exercise_files'

    if debug:
        print(f'The length of input_files is {len(input_files)}.\n')
        print(f'This is a new line ... {separator}')

    with open(os.path.join(output_file_destination, output_file), 'w') as f_out:

        for index, each_file in enumerate(input_files):
            with open(each_file) as f_in:

                for each_line in f_in:
                    print(each_line, file=f_out)
                if not index == len(input_files) - 1:
                    f_out.write(separator)

    return os.path.join(output_file_destination, output_file)

