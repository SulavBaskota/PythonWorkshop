"""
Q22. Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
"""


def func(s):
    digit = 0
    letter = 0
    for each in s:
        if 'A' <= each <= 'z':
            letter += 1
        elif '0' <= each <= '9':
            digit += 1
    print(f"LETTERS: {letter}")
    print(f"DIGITS: {digit}")


string_1 = input("Enter a string: ")
func(string_1)