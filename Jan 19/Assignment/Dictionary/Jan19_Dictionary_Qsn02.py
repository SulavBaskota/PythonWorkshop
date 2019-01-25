"""
2. Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""
dict_1 = {
    0: 10,
    1: 20
}
key = int(input("enter key: "))
val = int(input("enter value: "))
dict_1[key] = val
"dict_1.update({key: val})"  # Alternate solution

print(dict_1)
