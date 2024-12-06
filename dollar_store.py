#! /usr/bin/env python3

# Section 8, Exercise 10: Dollar Store

# Create a set of strings containing the items in your store.  Ask the user 
#   what they want to buy, continuing until they enter an empty string.  If 
#   they enter something in the store, acknowledge the action and increase the 
#   order total by one dollar. 
#   Let them know if the item they ask for is not in the store. 
#   When the user enters an empty string, provide the total and exit. 

debug = None

store = (set(['fish', 'rice', 'beans', 'lettuce', 'tomato', 'pepper', 'water',
              'soda', 'soap', 'toothpaste', 'shampoo', 'lipstick'] ))
order_total = 0

while True:
    if not order_total:
        item = input('Welcome to the store, what would you like to purchase? ').strip().lower()
    else:
        item = input('Would you like anything else? ').strip().lower()

    if not item:
        break
    elif item in store:
        print(f'{item} is available, everything costs a dollar.')
        order_total += 1
        print(f'Your store subtotal is {order_total} dollar(s), please continue to shop or press return / enter to finish.\n')
        continue
    else:
        print(f"Sorry, {item} is (are) not available, let's see if you would like something else.\n")
        continue

print(f"\nThanks for your purchase.  Your total is {order_total} dollar(s), we appreciate your business.")
