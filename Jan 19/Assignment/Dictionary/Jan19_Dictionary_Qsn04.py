"""
4. Write a Python script to check if a given key already exists in a dictionary.
"""
sample_dic = {
    'name': 'sulav',
    'age': 21,
    'nationality': 'nepalese',
    'home': 'lokanthali',
    'height': 5.9
}
key = input("Enter key: ")
print(sample_dic.get(key, 'Key not found'))
