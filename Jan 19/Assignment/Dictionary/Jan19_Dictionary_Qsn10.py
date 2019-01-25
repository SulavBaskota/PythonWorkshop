"""
10. Write a Python program to remove a key from a dictionary.
"""

dict_1 = {
    'name': "Sulav",
    'lastname': "Baskota",
    'section': 'A',
    'semester': 'First'
}

print(dict_1)
key = input("Enter a key: ")
if key in dict_1:
    del dict_1[key]
    print(dict_1)
else:
    print("Key not found.")

