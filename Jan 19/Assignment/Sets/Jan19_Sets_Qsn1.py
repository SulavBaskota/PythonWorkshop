"""
1. Write a Python program to create a set and demonstrate 7 methods that can be done with set
data structure.
"""
set_1 = set()
set_2 = set()
num = int(input("Enter the number of items in set_1: \t"))
for i in range(num):
    element = input("Enter element: \t")
    set_1.add(element)

print(f"set_1: {set_1}\n")

num2 = int(input("Enter the number of items in set_2: \t"))
for i in range(num2):
    element2 = input("Enter element: \t")
    set_2.add(element2)
print(f"set_2: {set_2}\n")

print(f"Intersection: {set_1.intersection(set_2)}\n")
print(f"Union: {set_1.union(set_2)}\n")
print(f"Difference: {set_1.difference(set_2)}\n")

print(f"set_1 superset of set_2 : {set_1.issuperset(set_2)}")
print(f"set_1 subset of set_2 : {set_1.issubset(set_2)}")

set_1.discard("sports")
print(f"set_1: {set_1}\n")

set_1.clear()
set_2.clear()
print(f"set_1: {set_1}\n")
print(f"set_2: {set_2}\n")

set_1.add('hello')
set_1.add('world')
set_2.add('sulav')

set_2.update(['baskota', 'python', 'DWIT'])

print(f"set_1: {set_1}\n")
print(f"set_2: {set_2}\n")
