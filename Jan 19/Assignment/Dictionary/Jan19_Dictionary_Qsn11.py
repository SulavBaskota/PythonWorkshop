"""
11. Write a Python program to sort a dictionary by key.
"""

import operator

dict_1 = {
    'name': "Sulav",
    'lastname': "Baskota",
    'section': 'A',
    'semester': 'First'
}
print(f"Original dictionary {dict_1}")
order = input("Enter 'A' for ascending and 'D' For descending: ")
if order == 'A':
    sorted_dict = sorted(dict_1.items(), key=operator.itemgetter(0))
    print(f"Ascending sort: {sorted_dict}")
else:
    sorted_dict = sorted(dict_1.items(), key=operator.itemgetter(0), reverse=True)
    print(f"Descending sort: {sorted_dict}")
