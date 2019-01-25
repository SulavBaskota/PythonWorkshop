"""
1. Write a Python function to find the Max of three numbers.
"""
def max(a, b):
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
print(f"The biggest number among {num1}, {num2}, {num3} is : {max(num3,max(num1,num2))}")

