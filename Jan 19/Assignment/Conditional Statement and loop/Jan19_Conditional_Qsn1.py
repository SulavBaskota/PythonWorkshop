"""
1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
between 1500 and 2700 (both included).
Date: 20 Jan, 2019
Author: Sulav Baskota
"""

for x in range(1500, 2701, 1):
    if x % 7 == 0:
        if x % 5 == 0:
            print(x)
