"""
5. Write a function called digit_sum that can take any mumber of intiger arguments and returns
the sum of all that number's digits.
"""
def digit_sum(*args):
    sum = 0
    for each in args:
        sum += each
    return sum

print(digit_sum(1,2,4,4,5,6,90,56))
print(digit_sum(56,67,435,23,23,45))
print(digit_sum(1,2))
print(digit_sum())