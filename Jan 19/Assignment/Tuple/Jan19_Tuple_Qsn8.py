"""
8. Write a Python program to sort a tuple by its float element.
Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
"""

list_1 = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sorted_d = sorted(list_1, key=lambda float_val: float(float_val[1]), reverse=True)
print(sorted_d)


