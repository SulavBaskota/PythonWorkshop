"""
Q11. Write a function that reads a text file words.txt and generate a dictionary that stores each
word as a key and number of letters in that word as a value. For example:
your words.txt file contains words like: Hello Python.
The output of your program should be dictionary like this: {“Hello”: 5, “Python”: 6}
"""


def gen_dic(name):
    dict_1 = {}
    f = open(name, 'r')
    for x in f:
        list_1 = x.split()
        for each in list_1:
            dict_1[each] = len(each)
        list_1 = []
    return dict_1


fname = input("Enter file name: ")
print(f"{gen_dic(fname)}")
