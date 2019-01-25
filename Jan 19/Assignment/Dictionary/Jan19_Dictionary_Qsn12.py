"""
12. Write a Python program to get the maximum and minimum value in a dictionary.
"""
dict_1 = {
    'physics': 28,
    'math': 36,
    'digital_logic': 29,
    'intro_to_it': 27,
    'english': 26,
    'c_programming': 19
}
'''
maxvalue = max(dict_1.keys(), key=lambda x: dict_1[x])
minvalue = min(dict_1.keys(), key=lambda x: dict_1[x])
print(f"Minimum value: {dict_1[minvalue]}")
print(f"Maximum value: {dict_1[maxvalue]}")
'''
minvalue = list(dict_1.values())[0]
maxvalue = 0
print(dict_1)
for each in dict_1.values():
    if each > maxvalue:
        maxvalue = each
    if each < minvalue:
        minvalue = each
print(f"Minimum value: {minvalue}")
print(f"Maximum value: {maxvalue}")
