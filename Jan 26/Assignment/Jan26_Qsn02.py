"""
Q2. check whether the number entered by the user is a strong number or not.
Strong Numbers are the numbers whose sum of factorial of digits is equal to the original number. Given
a number, check if it is a Strong Number or not.
Input: 145
Output: Yes
Sum of digit factorials = 1! + 4! + 5!
= 1 + 24 + 120
= 145
"""


def fact(a):
    if a == 1:
        return 1
    else:
        return a*fact(a-1)


num = input("Enter a number: ")
sum_fact = 0
for each in num:
    sum_fact += fact(int(each))

if sum_fact == int(num):
    print(f"{num} is a strong number.")
else:
    print(f"{num} is not a strong number.")
