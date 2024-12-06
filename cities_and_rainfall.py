#! /usr/bin/env python3

# Section 7, Exercise 9: Cities and Accumulating Rainfall

# Ask the user two questions, for a city, and for daily rainfall in that city.
#   Continue to ask the user for multiple cities and rainfall until they end
#   input in the usual manner.  Note that a user can enter multiple entries for 
#   a city, that is, for more than one day, so add the daily rainfall to the 
#   existing city each time (or start a new city as needed).  At the end, print 
#   all of the city and rainfall values.
#   Note leaving out the sorting in the json formatted dictionary preserves entry
#   order, which may be helpful for debugging or understanding processing.

# Faan DeSwardt suggested using some json based on what he sees in his work
import json

debug = None

total_rainfall = {}
city_name = ''
daily_rainfall = 0  # in mm hah, this is kind of a hint variable for what I called daily amount

while True:
    city_name = input('Please enter the name of a city: ').strip().title()

    if not city_name:
        break

    daily_amount = input('Please enter the rainfall for a day (whole mm): ').strip()

    if not daily_amount.isnumeric():
        print('We\'re encountering a problem with the numeric value, retrying with city name.\n')
        continue
    else:
        daily_rainfall = int(daily_amount)

    # Original implementation prior to checking approved solution
    #if not total_rainfall.get(city_name):
    #    total_rainfall[city_name] = int(daily_amount)
    #else:
    #    total_rainfall[city_name] += int(daily_amount)

    # Reuven demonstrated a previous way that works
    # if city_name in total_rainfall:
    #     total_rainfall[city_name] += daily_amount
    # else:
    #     total_rainfall[city_name] = daily_amount

    # Reuven had a snazzier way to do this as shown below or using <dictionary>.setdefault()
    # total_rainfall[city_name] = total_rainfall[city_name].setdefault(0)
    # total_rainfall[city_name] = total_rainfall[city_name] += daily_amount

    # Reuven's version using <dictionary>.get()
    total_rainfall[city_name] = total_rainfall.get(city_name, 0) + daily_rainfall

if debug:
    print(f'\nCurrent dictionary status:\n{json.dumps(total_rainfall, indent=2)}') # sort_keys=True,

print(f'\nRainfall totals for each city follow:')
for key, value in sorted(total_rainfall.items()):
    print(f'{key}: {value} mm')
