"""
Build a tip calculator app in Python. Logic being calculating a tip is as follows:
- if your bill is $ 43 and quality of service was 30% (satisfactory) and the waiter served 4
people, then tip amount will be: $3.23 by each person.
Formula: tip = (billed_amount * service_quality) / num_of_people_served
"""

exit_calc = False
while not exit_calc:
    billed_amount = float(input("Enter your bill: $"))
    num_of_people_served = int(input("Enter the number of people served: "))
    service_quality = int(input("Enter the quality of service: "))
    tip = (billed_amount * (service_quality / 100)) / num_of_people_served
    print(f"The tip amount is: ${tip}")
    again = input("Calculate again(Yes/No)?: ")
    if again == "No":
        exit_calc = True
