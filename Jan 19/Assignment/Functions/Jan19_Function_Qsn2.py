"""
2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
Expected Output : 20
"""
def get_sum(a):
    sum = 0
    for each in a:
        sum += each
    return sum

list_1 = list()
num_item = int(input("Enter the number of items in list: "))
for i in range(num_item):
    item = int(input("Enter list item: "))
    list_1.append(item)
print(f"The sum of all the items in list {list_1} is : {get_sum(list_1)}")

