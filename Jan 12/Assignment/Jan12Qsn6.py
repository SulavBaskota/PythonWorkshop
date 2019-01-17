"""
Q6. Write a python script to demonstrate at least 10 built in functions in Python.
Author: Sulav Baskota
Date: 16 Jan, 2019
"""
x=int(input("\nEnter a number to check it's absolute value: "))
abs_value=abs(x)
print(f"The absoulte value of number {x} is {abs_value}.")
binary_val = bin(x)
print(f"The binary value of number {x} is {binary_val}.")
print("The value {} is greater than 0:  {}".format(x , bool((x)>0)))


y=int(input("\nEnter a number: "))
z=int(input("Enter a number: "))
quo_rem=divmod(y,z)
print(f"The value of {y}//{z} is {quo_rem[0]} and the value of {y}%{z} is {quo_rem[1]}.")
print("The data type of returned by function devmod() is: ")
print(type(quo_rem))
power=pow(y,z)
print(f"The value of {y} raised to the power of {z} is {power}.")

name=input("\nEnter a name: ")
length = len(name)
print(f"The length of string {name} is {length}.")
sliced_name=slice(1,4)
print("Sliced name {} from position 1 to 3 is {}.".format(name,name[sliced_name]))


text=input("\nEnter a text: ")
sorted_text=sorted(text.split(),key=str.lower)
print(f"The text '{text}' sorted in ascending order is {sorted_text}.")
print("The data type of variable sorted-name is: ")
print(type(sorted_text))

list_1=[16,45,56.6,-98,345,-87.5]
print("\nThe intitial order of list is: {}.".format(list_1))
list_1.sort()
print("The sorted list is: {}.".format(list_1))


num = input("\nEnter a Number: ")
num = int(num)
print("The ascii character equivalent of integer {} is '{}'.".format(num,chr(num)))



