import random

def get_random_number_multiplied(n=1):
    return random.random()*n

class Card:
    def __init__(self, initiative):
        self.initiative = initiative