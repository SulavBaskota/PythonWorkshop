"""
5. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Note : Use 'continue' statement.
Expected Output : 0 1 2 4 5
"""
for each in range(0, 6):
    if each == 3 or each == 6:
        continue
    else:
        print(each)
