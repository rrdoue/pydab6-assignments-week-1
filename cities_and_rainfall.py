#! /usr/bin/env python3

# Section 7, Exercise 9: Cities and Accumulating Rainfall

# Ask the user two questions, for a city, and for daily rainfall in that city.
#   Continue to ask the user for multiple cities and rainfall until they end
#   input in the usual manner.  Note that a user can enter multiple entries for 
#   a city, that is, for more than one day, so add the daily rainfall to the 
#   existing city each time (or start a new city as needed).  At the end, print 
#   all of the city and rainfall values.

debug = None

rain = {}
city = ''
total_rainfall = 0 # in mm hah

while True:
    city = input('Please enter the name of a city: ').strip().title()

    if not city:
        break

    amount = input('Please enter the rainfall for a day (whole mm): ').strip()

    if not amount.isnumeric():
        amount = input('Rainfall amount is not a whole number, please try again: ')

    if not rain.get(city):
        rain[city] = int(amount)
    else:
        rain[city] += int(amount)
    
    print('\n')

for key, value in rain.items():
    print(f'The total rainfall for {key} is {value} mm.')

