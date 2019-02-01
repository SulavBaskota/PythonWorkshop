"""
Q8. Two words are anagrams if you can rearrange the letters from one to spell the other.
Write a function called is_anagram that takes two strings and returns True if they are anagrams.
"""


def is_anagram(a, b):

    for each in a:
        flag = False
        for val in b:
            if each == val:
                flag = True
        if not flag:
            return False
    return True


str_1 = input("Enter a string: ")
str_2 = input("Enter another string: ")
print(is_anagram(str_1, str_2))

