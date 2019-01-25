"""
3. Write a Python program to get a string from a given string where all occurrences of its first
char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
"""
str_1 = input("Enter a string: ")

new_list = list()
new_list.append(str_1[0])
for each in str_1[1:]:
    if each == str_1[0]:
        new_list.append('$')
    else:
        new_list.append(each)
new_str = "".join(new_list)
print(new_str)
"""
list_1 = []
for each in str_1:
    list_1.append(each)
index = 1
for each in list_1[1:]:
    if each == list_1[0]:
        list_1[index] = '$'
    index += 1
new_str = ''.join(list_1)
print(new_str)
"""
