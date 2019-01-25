"""
5. Write a Python program to remove an item from a tuple.
"""
tup = (1, 2, 3, 26, 27, 78, 10)
print(tup)
item = int(input("enter a item you want to remove form the tuple: "))
list_1 = list(tup)
list_1.remove(item)
tup = tuple(list_1)
print(tup)
