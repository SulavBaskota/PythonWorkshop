"""
Q14. Write recursive function to calculate fibonacci number
fibonacci series = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
"""
# the term 0 of the series is considered to be 0
def fibno(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibno(n-1) + fibno(n-2)

nth = int(input("Enter the term of the series: "))
print(fibno(nth))