"""
7. Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""
list_1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list_2 = []
for each in list_1:
    temp_list = list(each)
    temp_list[-1] = 100
    tup = tuple(temp_list)
    list_2.append(tup)
print(list_2)

"""
# print([tup[:-1]+(100,) for tup in list_1])
"""
