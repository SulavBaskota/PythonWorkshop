"""
6. Write a Python program to print a tuple with string formatting.
Sample tuple : (100, 200, 300)
Output : This is a tuple (100, 200, 300)
"""
tup = (100, 200, 300)
print(f"This is a tuple {tup}")
print("This is a tuple {}".format(tup))
print("This is a tuple {0}".format(tup))
print("This is a tuple {tup_key}".format(tup_key=tup))
