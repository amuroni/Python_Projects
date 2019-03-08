"""this is going to be the DIE class, that represents a single die"""

from random import randint


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides  # die has six faces

    def roll(self):
        return randint(1, self.num_sides)  # roll and get a random value

