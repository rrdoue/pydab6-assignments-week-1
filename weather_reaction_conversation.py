#! /usr/bin/python3

# Section 1, Exercise: weather reaction conversation

response = input('What\'s the weather like there?:  ')

if (response == 'rain' or 
    response == 'snow'):
    print(f'Wow, it looks like bad weather for your area.')
elif response == 'sun':
    print(f'That\'s nice, I hope it\'s a comfortable temperature for you.')
else:
    print(f'Hmm, I don\'t know what to say about "' + response + '".')

