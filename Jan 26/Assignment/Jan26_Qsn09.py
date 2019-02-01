"""
Q9. Write a class which has a staticmethod called password_generator. This method takes in an
integer parameter which is the length of the password. Upon invoking the method, it should
generate a random password.
Example:
ClassName. password_generator(8)
dSAd4#@)
"""
import random


class PasswordGenerator:

    @staticmethod
    def password_generator(intlen):
        characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                      'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5',
                      '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '&', '*', '(', ')']
        password = []
        for i in range(intlen):
            password.append(characters[random.randint(1,70)])
        password = "".join(password)
        return password


length = int(input("Enter length of password: "))
print(f"Your password is : {PasswordGenerator.password_generator(length)}")
