"""
3. Write a Python function to calculate the factorial of a number (a non-negative integer). The
function accepts the number as an argument.
"""


def fact(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fact(num - 1)


num_1 = int(input("Enter a number: "))
if num_1 < 0:
    print("Invalid number.")
else:
    print(f"The factorial is : {fact(num_1)}")


