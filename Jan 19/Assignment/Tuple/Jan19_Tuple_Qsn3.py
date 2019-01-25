"""
3. Write a Python program to check whether an element exists within a tuple.
"""
tup = (1, 2, 3, 500, 700, 88, 10)
item = int(input("Enter a item: "))
print(f"The element exists within the tuple: { item in tup }")
