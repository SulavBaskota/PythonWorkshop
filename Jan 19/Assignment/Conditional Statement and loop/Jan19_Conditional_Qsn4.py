"""
4. Write a Python program to count the number of even and odd numbers from a series of
numbers.
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
Expected Output :
Number of even numbers : 5
Number of odd numbers : 4
"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for each in numbers:
    if each % 2 == 0:
        even += 1
    else:
        odd += 1
print(f"The no of even numbers in the series: {even}")
print(f"The no of odd numbers in the series: {odd}")
