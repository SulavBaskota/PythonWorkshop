"""
Q5. Write a function called nested_sum that takes a list of lists of integers and adds up
the elements from all of the nested lists. For example:
t = [[1, 2], [3], [4, 5, 6]]
nested_sum(t)
21
"""


def nested_sum(n):
    sum_1 = 0
    for each in n:
        for i in each:
            sum_1 += i
    return sum_1


# Method 2
"""
def nested_sum(n):
    sum_1 = 0
    for each in n:
        if type(each) == int:
            sum_1 += each
        else:
            sum_1 += nested_sum(each)
    return sum_1

"""


# Method 3
"""
def nested_sum(n):
    sum_1 = 0
    for each in n:
        sum_1 += sum(each)
    return sum_1
"""

t = [[1, 2], [3], [4, 5, 6]]
print(f"The sum is {nested_sum(t)}")
