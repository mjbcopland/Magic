class Spell:
    def __init__(self, effect, action, shape, target):
        self.spell_effect = effect  # Tile-wide effect
        self.action_type = action # What the spell does - create/display/destory
        self.shape = shape
        self.target = target
        self.affix = None

    def cost(self):
        return
