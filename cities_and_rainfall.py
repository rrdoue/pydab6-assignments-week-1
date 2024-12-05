#! /usr/bin/env python3

# Section 7, Exercise 9: Cities and Accumulating Rainfall

# Ask the user two questions, for a city, and for daily rainfall in that city.
#   Continue to ask the user for multiple cities and rainfall until they end
#   input in the usual manner.  At the end, print each city and the total
#   rainfall to date.

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
        amount = input('Rainfall amount is not a number, please try again: ')
        continue

    # value = rain.get(city)
    # if not value:
    #     rain[city] = int(amount)
    # else:
    #     rain[city] += int(amount)

    if not rain.get(city):
        rain[city] = int(amount)
    else:
        rain[city] += int(amount)

print(f'\nRainfall totals for each city follow:')
for key, value in sorted(rain.items()):
    print(f'{key}: {value} mm')

