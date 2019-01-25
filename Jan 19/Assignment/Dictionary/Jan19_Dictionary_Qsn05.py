"""
5. Write a Python program to iterate over dictionaries using for loops.
"""
dict_1 = {
    'name': "Sulav",
    'age': 20,
    'section': 'A',
    'semester': 'First'
}
for key, val in dict_1.items():
    print(f"{key} : {val}")


dict_2 = {
    'Nepal': {'capital': 'Kathmandu', 'Population': 300000000},
    'China': {'capital': 'Beijing', 'Population': 1000000000}
}
for country, info in dict_2.items():
    print(f"{country}")
    for key, val in info.items():
        print(f"{key} : {val}")
