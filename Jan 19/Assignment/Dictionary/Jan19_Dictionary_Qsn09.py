"""
9. Write a Python program to multiply all the items in a dictionary.
"""
dict_1 = {
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25
}
prod = 1
for each in dict_1.values():
    prod *= each
print(f"The product of all the values of the dictionary is : {prod}")
