#! /usr/bin/env python3

# Section 7, Exercise 8: Restaurant Menu

# Ask the user for their order, or what would they like to order.  If the item 
#   is available, based on a dictionary of item keys and value prices, add the 
#   item to the order and include the price in the total price.  When the user 
#   enters a return to stop the order, print the total cost.

debug = None

# Define a menu of items as a dictionary
# Format is 'key':value, where spaces between the semicolon and key / value 
#   appear to be allowed
# Values are integers, but could nearly as easily be floating-point numbers
menu = ({'sandwich':5, 'chips':3, 'water':0, 'soda':2, 'brownie':3, 'cookie':3, 
         'salad':4, 'guatemalan chicken':6, 'small planet burger':6, 
         'smoothie':5, 'milk':3, 'coffee':2, 'tea':2})

# Define a total as an integer (could be float also)
total = 0
# Define an order as a list, where we will append to the order as a person adds 
#   items from the menu
order = [ ]

while True:
    if not order:
        item = input('Welcome to the Good Earth Restaurant, what would you like to order? ').strip().lower()
    else:
        item = input('Would you like anything else? ').strip().lower()

    if not item:
        break
    if item in menu:
        print(f"{item} is available.")
        order.append(item)
        total += menu[item]
        if debug:
            print(order);
        print(f"You've ordered a {', '.join(order)}.")
        print(f'Your menu subtotal is {total}, please continue your order or press return / enter to finish.\n')
        continue
    else:
        print(f"Sorry, {item} is (are) not available, let's see if you would like something else.\n")
        continue

if not order:
    print(f"\nSorry if we misunderstood you or you couldn't find anything you liked.")
    print(f"Perhaps you can return and give us another opportunity to serve you.\n")
else:
    print(f"\nThanks for ordering the {len(order)} items listed above. Your menu total is {total}, it's nice having you here.")

