import random

def roll_dices():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1, dice2, dice1 + dice2

    
