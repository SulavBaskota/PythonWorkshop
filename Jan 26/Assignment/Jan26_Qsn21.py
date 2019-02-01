"""
Q21. Write a program that accepts a sentence and calculate the number of upper case letters and lower
case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
"""


def func(s):
    ucase = 0
    lcase = 0
    for each in s:
        if 'a' <= each <= 'z':
            lcase += 1
        elif 'A' <= each <= 'Z':
            ucase += 1
    print(f"LOWER CASE: {lcase}")
    print(f"UPPER CASE: {ucase}")


string_1 = input("Enter a string: ")
func(string_1)
