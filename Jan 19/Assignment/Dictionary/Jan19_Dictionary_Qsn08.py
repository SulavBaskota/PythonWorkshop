"""
8. Write a Python program to sum all the items in a dictionary.
"""

dict_1 = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
dict_2 = {
    'name': "Sulav",
    'Lastname': "Baskota",
    'section': 'A',
    'semester': 'First'
}
sum_val = 0

for val in dict_1.values():
    sum_val += val
print(f"The sum of all the values is : {sum_val}")

sum_val = ""
for val in dict_2.values():
    sum_val += val
print(f"The sum of all the values is : {sum_val}")
