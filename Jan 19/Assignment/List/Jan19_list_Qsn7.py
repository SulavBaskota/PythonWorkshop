"""
7. Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
"""
list_1 = [1, 2, 3, 4]
index = 0
for each in list_1:
    list_1[index] = 'emp' + str(each)
    index += 1
print(f"New list: {list_1}")
