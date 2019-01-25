"""
2. Create a for loop that prompts the user for a hobby 3 times, then appends each one to
hobbies.
"""
num = 3
hobby = list()
for x in range(num):
    x = input("Enter a hobby: ")
    hobby.append(x)
print(f"Your hobbies are:\n {hobby}")

