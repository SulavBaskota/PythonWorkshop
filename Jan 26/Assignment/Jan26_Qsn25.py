"""
Q25. Define a function that takes in a List of numbers and produces another list with squared value.
squarelist([1,2,3]) should produce [1, 4, 9]
squarelist([1,4,9]) should produce [1, 16, 81]
"""


def squarelist(lis):
    new_list2 = []
    for each in lis:
        new_list2.append(each**2)
    return new_list2


num = int(input("enter the number of items in list: "))
list_1 = []
for i in range(num):
    item = int(input("Enter item: "))
    list_1.append(item)
new_list = squarelist(list_1)
print(f"Square list: {new_list}")
