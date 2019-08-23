from Spell import Spell, ActionType
from Element import ElementType


class Caster:
    def __init__(self):
        self.current_mana = None
        self.max_mana = None

    def cast_spell(self):
        print("Casting default fire spell.")
        spell = Spell(ElementType.Fire, [0, 0], "circle", ActionType.CREATE)
        return spell.cast()


