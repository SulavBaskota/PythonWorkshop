"""
Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
# the term 0 of the series is considered to be 0
"""


def fibno(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibno(n-1) + fibno(n-2)


nth = int(input("Enter the term of the series: "))
print(fibno(nth))
