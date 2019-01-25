"""
7. Write a Python script to merge two Python dictionaries.
"""


def merge_dict(*args):
    new_dict = {}
    for each in args:
        new_dict.update(each)

    return new_dict


dict_1 = {
    'name': "Sulav",
    'age': 20,
    'section': 'A',
    'semester': 'First'
}
dict_2 = {
    'Nepal': {'capital': 'Kathmandu', 'Population': 300000000},
    'China': {'capital': 'Beijing', 'Population': 1000000000}
}
dict_3 = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
print("Merging dict_1 and dict_2:")
print(merge_dict(dict_1, dict_2))

print("Merging dict_2 and dict_3:")
print(merge_dict(dict_2, dict_3))

print("Merging dict_1 and dict_3:")
print(merge_dict(dict_1, dict_3))

print("Merging dict_1 and dict_2 and dict_3:")
print(merge_dict(dict_1, dict_2, dict_3))