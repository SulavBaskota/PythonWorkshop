"""
Q6. Write a function called cumulative_sum that takes a list of numbers and returns the cumu-
lative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the

original list. For example:
t = [1, 2, 3]
cumsum(t)
[1, 3, 6]
"""


def cummulative_sum(n):
    cum_list = []
    sum_1 = 0
    for each in n:
        sum_1 += each
        cum_list.append(sum_1)
    return cum_list


t = [1, 2, 3]
print(f"original list: {t}")
print(f"Cummulative sum list: {cummulative_sum(t)}")
