"""
Q23. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""


class StringMethod:

    def __init__(self):
        self.string_1 = ""

    def getstring(self):
        self.string_1 = input("Enter a string: ")

    def printstring(self):
        print(f"{self.string_1.upper()}")


str1 = StringMethod()
str1.getstring()
str1.printstring()
