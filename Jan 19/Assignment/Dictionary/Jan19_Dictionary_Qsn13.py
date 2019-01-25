"""
13. Write a Python program to remove duplicates from Dictionary.
"""
dict_1 = {
    'country1': {'name': 'Nepal', 'capital': 'kathmandu'},
    'country2': {'name': 'China', 'capital': 'Beijing'},
    'country3': {'name': 'Nepal', 'capital': 'kathmandu'},
    'country4': {'name': 'India', 'capital': 'New Delhi'},
    'country5': {'name': 'China', 'capital': 'Beijing'}
}
new_dict = {

}


""" #Alternative Solution:
for key, val in dict_1.items():
    if val not in new_dict.values():
        new_dict[key] = val
print(new_dict)
"""

for key, val in dict_1.items():
    repeated_value = False
    for each in new_dict.values():
        if each == val:
            repeated_value = True
    if not repeated_value:
        new_dict[key] = val
print(new_dict)
