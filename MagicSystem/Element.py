from enum import Enum


class ElementType(Enum):
    Fire = 1
    Water = 2
    Earth = 3
    Lightning = 4
    Sound = 5
    Light = 6
    Life = 7
    Time = 8
    Gravity = 9
    Space = 10
    Psychic = 11
    Mana = 12


class Element:
    def __init__(self):
        self.Type = None

    def set_element(self, elementtype):
        self.Type = elementtype
