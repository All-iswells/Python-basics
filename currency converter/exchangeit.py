"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Eric Robertson
Date: May 11th, 2024
"""
import currency

start_currency = input('3-letter code for original currency: ')
target_currency = input('3-letter code for the new currency: ')
start_amt = float(input('Amount of the original currency: '))

new_amt = round(currency.exchange(start_currency,target_currency,start_amt), 3)

result = 'You can exchange ' + str(start_amt) + ' ' + start_currency + ' for ' + str(new_amt) +\
 ' ' + target_currency + '.'
print(result)