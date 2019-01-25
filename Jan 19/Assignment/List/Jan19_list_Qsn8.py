"""
8. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]
"""

parent_list = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
greatest_sum = 0
greatest_index = 0
for index, child_list in enumerate(parent_list):
    sum_items = 0
    for each in child_list:
        sum_items += each
    if sum_items > greatest_sum:
        greatest_sum = sum_items
        greatest_index = index
print(f"The list in a list of lists whose sum of elements is the highest is : {parent_list[greatest_index]}")

""" #Alternate : by storing the sum of each list
parent_list = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
sum_list = []
for child_list in parent_list:
    sum_items = 0
    for each in child_list:
        sum_items += each
    sum_list.append(sum_items)

greatest_sum = sum_list[0]
for each in sum_list[1:]:
    greatest_sum = each if each > greatest_sum else greatest_sum
greatest_index = sum_list.index(greatest_sum)
print(f"The list in a list of lists whose sum of elements is the highest is : {parent_list[greatest_index]}")

"""
