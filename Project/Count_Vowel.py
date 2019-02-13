"""
Enter a string and the program counts the number of vowels in the text.
For added complexity have it report a sum of each vowel found.
"""
str_1 = input("Enter a string: ")
vowel = 0
str_dict = {}
for each in str_1:
    if each == 'a' or each == 'e' or each == 'i' or each == 'o' or each == 'u':
        str_dict[each] = str_1.count(each)
        vowel = vowel + 1
print(f"Total number of vowel : {vowel}")
print(str_dict)

