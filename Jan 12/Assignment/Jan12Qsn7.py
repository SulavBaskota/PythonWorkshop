"""
Q7. Write a function called disect that takes a list, modifies it by removing the first and last elements
Author: Sulav Baskota
Date: 17 Jan, 2019
"""

# Three method to solve this question.
# Function Type 1:
 
def disect(t):
    del t[0]
    if(len(t)-1>0):
        del t[len(t)-1]
    return t

#Function Type 2:
"""
def disect(t):
    t.remove(t[0])
    if(len(t)-1>0):
        t.remove(t[len(t)-1])
    return t
"""
#Function Type 3:
"""
def disect(t):
    t = t[1:len(t)-1]
    return t
"""
List_1 = list()

num_item = int(input("Enter the number of elements in list: "))


for x in range(num_item):
    list_item = input("Enter item to insert in list: ")
    List_1.append(list_item)

print("Original List: {}".format(List_1))

List_1 = disect(List_1)
print("Modified List: {}".format(List_1))    


