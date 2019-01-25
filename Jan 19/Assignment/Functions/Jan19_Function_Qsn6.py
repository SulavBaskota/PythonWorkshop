"""
6. Write a Python function that accepts a string and calculate the number of upper case letters
and lower case letters.
Sample String : 'The quick Brow Fox'

Expected Output :
No. of Upper case characters : 3
No. of Lower case Characters : 12
"""
def count_string(text):
    ucase = 0
    lcase = 0
    for each in text:
        if 'a' <= each <= 'z':
            lcase += 1
        elif 'A' <= each <= 'Z':
            ucase += 1

    print(f"No. of Upper case characters: {ucase}")
    print(f"No. of Lower case charactersL {lcase}")

str_1 = input("Enter a string: ")
count_string(str_1)
