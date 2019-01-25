"""
8. Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each
dog year equals 4 human years.
Expected Output:
Input a dog's age in human years: 15
The dog's age in dog's years is 73
"""
dog_age = int(input("Input a dog's age in human years: "))
dog_year = 0
for i in range(1, dog_age+1):
    if i <= 2:
        dog_year += 10.5
    else:
        dog_year += 4
print(f"The dog's age in dog's year is {dog_year}")
