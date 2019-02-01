"""
Q10. Simute a rolling dice using class
"""

import random


class Dice:

    @staticmethod
    def dice_roll():
        return int(random.random()*6)+1


exit_1 = False
while not exit_1:
    choice = input("ROll dice? (Y/N)\n")
    if choice == "Y" or choice == "y":
        print(Dice.dice_roll())
    else:
        exit_1 = True
