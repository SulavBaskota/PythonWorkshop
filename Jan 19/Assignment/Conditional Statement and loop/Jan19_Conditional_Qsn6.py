"""
6. Write a Python program which takes two digits m (row) and n (column) as input and
generates a two-dimensional array. The element value in the i-th row and j-th column of the
array should be i*j.
Note :
i = 0,1.., m-1
j = 0,1, n-1.
Test Data : Rows = 3, Columns = 4
Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
"""
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
"""
a = [[i * j for j in range(n)] for i in range(m)]
print(a)

"""
a = [[0] * n for i in range(m)]
'# a = [[0 for j in range(n)] for i in range(m)]'
print(a)
for i in range(m):
    for j in range(n):
        a[i][j] = i * j
print(a)
