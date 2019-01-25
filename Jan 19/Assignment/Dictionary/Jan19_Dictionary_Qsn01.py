"""
1. Write a Python script to sort (ascending and descending) a dictionary by value.
"""
dict_1 = {}
num_entry = int(input("Enter the number of dictionary entry: \t"))
for i in range(num_entry):
    entry = input("Enter dictionary entry: ")
    dict_1[i] = entry
print(f"Original dictionary : {dict_1}")

# Method 1
"""
import operator
sorted_dict = sorted(dict_1.items(), key=operator.itemgetter(1))  

# here (1) represents position of item in the dictionary that is being used to sort i.e. value of dictionary.

print(f"Ascending: {sorted_dict}")
rev_sorted = sorted(dict_1.items(), key=operator.itemgetter(1), reverse=True)
print(f"Descending: {rev_sorted}")
"""

# Method 2

sorted_dict = sorted(dict_1.items(), key=lambda x: x[1])
'x[1] represents that the item in position 1 is being used to sort i.e. value item of dictionary.'
print(f"Ascending: {sorted_dict}")
rev_sorted = sorted(dict_1.items(), key=lambda y: y[1], reverse=True)
print(f"Descending: {rev_sorted}")
