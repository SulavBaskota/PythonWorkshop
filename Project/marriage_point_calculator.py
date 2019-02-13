"""
Build marriage point calculator in Python.
"""
value_point = int(input("Enter the value of a point: Rs. "))
total_valid_maal = int(input("Enter the total valid maal: "))
saw_joker = int(input("Enter '1' in the case you saw the joker and '0' in the case you did not.: "))
if saw_joker == 0:
    net_loss = value_point * (total_valid_maal + 10)
    print(f"you have to pay a total of : Rs. {net_loss}")
else:
    num_of_player = int(input("Enter the total number of players: "))
    your_maal = int(input("Enter your maal: "))
    net_loss = ((total_valid_maal + 3) - (your_maal * num_of_player)) * value_point
    if net_loss < 0:
        print(f"You won: Rs. {net_loss * -1}")
    else:
        print(f"you have to pay a total of : Rs. {net_loss}")
