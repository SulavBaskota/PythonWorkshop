"""
2. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : 'google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
str_1 = input("Enter a string: ")
str_dict = {}
for each in str_1:
    str_dict[each] = str_1.count(each)
print(str_dict)

