#! /usr/bin/env python3

# Section 5, Exercise 1, Sum and Average Numbers from a User
# Request numbers from a user, then when they stop by entering an empty string, 
#   find the sum and average of the numbers. 

debug = None

total = 0
average = 0
number_list = [ ] # Reuven used a space inside the square brackets for an 
                  #   empty list

while True:
    value = input('Please enter a whole number (or leave blank to end input): ').strip()
    if value:
        if value.isnumeric():
            number_list.append(int(value))
        else:
            print('The value you provided is not a number, please try again, or leave the input blank to end input.')
            continue
    else:
        break

total = sum(number_list)

average = round(total / len(number_list), 2)

print(f'\nThe sum of the numbers is {total}.')
print(f'The average of the numbers is {average}.')

