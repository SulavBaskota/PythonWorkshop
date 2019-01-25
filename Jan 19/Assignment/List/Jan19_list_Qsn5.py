"""
5. Write a Python program to convert list to list of dictionaries.
Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000",
"#FFFF00"]
Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red',
'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name':
'Yellow', 'color_code': '#FFFF00'}]
"""

list_1 = ["Black", "Red", "Maroon", "Yellow"]
list_2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
new_list = []
dict_1 = {}
for each in range(len(list_1)):
    dict_1['color_name'] = list_1[each]
    dict_1['color_code'] = list_2[each]
    new_list.append(dict_1)
    dict_1 = {}

print(new_list)


""" # Alternate solution : using zip
color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])
"""

""" #Alternate solution : using tuple and dict() function
list_1 = ["Black", "Red", "Maroon", "Yellow"]
list_2 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
new_list = []
a = []
tuple_1 = ("color_name",)
tuple_2 = ("color_code",)
for each in range(len(list_1)):
    tuple_1 = tuple_1 + (list_1[each],)
    tuple_2 = tuple_2 + (list_2[each],)
    a.append(tuple_1)
    a.append(tuple_2)
    dict_1 = dict(a)
    new_list.append(dict_1)
    tuple_1 = ("color_name",)
    tuple_2 = ("color_code",)
    a =[]
print(new_list)
"""

