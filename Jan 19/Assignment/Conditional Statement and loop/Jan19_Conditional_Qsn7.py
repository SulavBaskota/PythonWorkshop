"""
7. Write a Python program to check the validity of password input by users.
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""
character = ('$', "#", '@')
has_s_letter = False
has_u_letter = False
has_digit = False
has_character = False
valid_length = False


password = input("Enter password: ")

for each in password:
    if 'a' <= each <= 'z':
        has_s_letter = True
    elif '0' <= each <= '9':
        has_digit = True
    elif 'A' <= each <= 'Z':
        has_u_letter = True
    else:
        for new in character:
            if new == each:
                has_character = True

if 6 <= len(password) <= 16:
    valid_length = True

if has_s_letter and has_u_letter and has_digit and has_character and valid_length:
    print("Password is valid.")
else:
    print("Invalid password.")
