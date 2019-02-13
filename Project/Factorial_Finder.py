"""
The Factorial of a positive integer, n, is defined as the product of the sequence n, n-1, n-2, ...1 and
the factorial of zero, 0, is defined as being 1.
Solve this using both loops and recursion.
"""

# method 1: Using recursion


def fact(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fact(num - 1)


print("Using recursion")
num_1 = int(input("Enter a number: "))
if num_1 < 0:
    print("Invalid number.")
else:
    print(f"The factorial is : {fact(num_1)}")


# method 2: Using a loop

print(f"Using loop")
num_2 = int(input("Enter a number: "))
factorial = 1
if num_2 < 0:
    print("Invalid Number.")
else:
    for each in range(1, num_2+1):
        factorial *= each
    print(f"The factorial is {factorial}")
