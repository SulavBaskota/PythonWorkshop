"""
Q7. Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements. For example:
t = [1, 2, 3, 4]
middle(t)
[2, 3]
"""


def middle(l):
    del l[0]
    if len(l) >= 1:
        del l[-1]
    return l


t = [1, 2, 3, 4]
print(f"new list: {middle(t)}")
