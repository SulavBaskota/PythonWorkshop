"""
15. Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

Sample_Data = [{"V": "S001"},
               {"V": "S002"},
               {"VI": "S001"},
               {"VI": "S005"},
               {"VII": "S005"},
               {"V": "S009"},
               {"VIII": "S007"}]

unique_val = set()
for each in Sample_Data:
    for val in each.values():
        unique_val.add(val)
print(unique_val)
''' #Alternative Solution:
unique_val = set(val for each in Sample_Data for val in each.values())
print(unique_val)
'''
