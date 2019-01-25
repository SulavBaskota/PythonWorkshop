"""
1. Write a Python program to calculate the length of a string. Do not use built-in len() function.
"""

str_1 = input("Enter a String: ")
len_str_1 = 0
for each in str_1:
    len_str_1 += 1
print(f"The length of string {str_1} is : {len_str_1}")
