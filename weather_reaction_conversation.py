#! /usr/bin/env python3

# Note: To run the most easily from a command line, use the syntax python3 <file_name>
# Or ensure the file is executable, then include a `./` before the file name.  
# For example, 
# chmod +x <file_name>
# or chmod u+x <file_name>
# Then,
# ./<file_name>

# Section 1, Exercise: weather reaction conversation

response = input('What\'s the weather like there?:  ')

if (response == 'rain' or 
    response == 'snow'):
    print(f'Wow, it looks like bad weather for your area.')
elif response == 'sun':
    print(f'That\'s nice, I hope it\'s a comfortable temperature for you.')
else:
    print(f'Hmm, I don\'t know what to say about "' + response + '".')

