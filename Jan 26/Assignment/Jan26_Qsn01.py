"""
Q1. check whether a number (entered by the user) is a perfect number or not.
A perfect number, a positive integer that is equal to the sum of its proper divisors. The smallest perfect
number is 6, which is the sum of 1, 2, and 3.
Input: 6
Proper divisors of 6 are: 1, 2 and 3
Sum of proper divisors = (1 + 2 + 3) which is equal to 6 (our input)
Hence, 6 is perfect number
"""

num = int(input("Enter a number: "))
prop_divisors = []

for i in range(1, num):
    if num % i == 0:
        prop_divisors.append(i)

sum_prop = 0

for each in prop_divisors:
    sum_prop += each

if sum_prop == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
