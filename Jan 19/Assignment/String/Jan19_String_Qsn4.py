"""
4. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given
string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""
str_1 = input("Enter a string: ")
new_str = str()
if len(str_1) < 3:
    print(str_1)
else:
    if str_1[-3:] == "ing":
        new_str = str_1 + "ly"
    else:
        new_str = str_1 + "ing"
print(new_str)
