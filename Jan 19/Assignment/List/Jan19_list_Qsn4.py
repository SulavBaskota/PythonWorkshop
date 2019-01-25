"""
4. Write a Python program to create a list by concatenating a given list which range goes from 1
to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""
num = int(input("Enter number of items in the list: "))
list_1 = []
for each in range(num):
    item = input("Enter item: ")
    list_1.append(item)
new_list = []
n = int(input("Enter a number: "))
for each in range(1, n+1):
    for new in list_1:
        new_list.append(new + str(each))
print(f"New list: {new_list}")
