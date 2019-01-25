"""
4. Define a function is_even that will take a number x as input.If x is even, then return True.
Otherwise, return False.
"""
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
num = int(input("Enter a number: "))
print(f"{num} is even?: {is_even(num)}")
