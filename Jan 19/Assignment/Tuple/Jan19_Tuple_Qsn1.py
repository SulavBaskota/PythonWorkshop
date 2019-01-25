"""
1. Write a Python program to add an item in a tuple.
"""
tup = ()
num = int(input("Enter the number of items: "))
for i in range(num):
    item = input("Enter item to be added: ")
    tup = tup + (item,)
print(f"{tup}")
