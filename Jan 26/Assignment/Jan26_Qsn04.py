"""
Q4. check whether a number entered by the user is magic number or not. The user will enter
1729 input number and program will calculate and check if it is magic number or not and print
on the console.
What is the magic number?
Input: 1729

Sum of digits of the given number.(1 + 7 + 2 + 9 => 19)
The reverse of 19 is 91
The product of digit sum and the reverse of digit sum.(19 X 91 = 1729)
If the product value and the given input are same,
then the given number is a magic number.(19 X 91 <=> 1729)
Output: So, 1729 is a magic number.
"""


def magic_prod(n):
    sum_1 = 0
    while n != 0:
        sum_1 += (n % 10)
        n = int(n/10)
    reverse = 0
    sum_2 = sum_1
    while sum_1 != 0:
        reverse = reverse * 10 + (sum_1 % 10)
        sum_1 = int(sum_1 / 10)
    return sum_2 * reverse


num = int(input("Enter a number: "))
n2 = magic_prod(num)

if n2 == num:
    print(f"{num} is magic number.")
else:
    print(f"{num} is not a magic number.")
