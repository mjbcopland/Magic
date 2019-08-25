from magic.elements import Fire, Water, Lightning
from util.enums import make_enum


EffectType = make_enum("EffectType", ("Fire", "Cold", "Lightning", "Earth", "Time"))

SettingType = make_enum("SettingType", ("Temperature", "Power", "Weight", "Rate"))


class Effect:
    def __init__(self, level, effect_type=None, setting_type=None, base_cost=None):
        self.type = effect_type
        self.setting_type = setting_type
        self.base_cost = base_cost
        self.start = None
        self.level = level

    @property
    def cost(self):
        return self.base_cost


class FireEffect(Effect):
    def __init__(self, level):
        super().__init__(
            level,
            effect_type=EffectType.FIRE,
            setting_type=SettingType.TEMPERATURE,
            base_cost=1,
        )

    def create(self, shape, position, velocity):
        temperature = 400 + (self.level * 100)
        return Fire(temperature, position, velocity, shape)


class ColdEffect(Effect):
    def __init__(self, level):
        super().__init__(
            level,
            effect_type=EffectType.COLD,
            setting_type=SettingType.TEMPERATURE,
            base_cost=1,
        )

    def create(self, shape, position, velocity):
        temperature = self.level * -25
        return Water(temperature, position, velocity, shape)


class LightningEffect(Effect):
    def __init__(self, level):
        super().__init__(
            level,
            effect_type=EffectType.LIGHTNING,
            setting_type=SettingType.POWER,
            base_cost=1,
        )

    def create(self, shape, position, velocity):
        power = self.level * 100
        return Lightning(power, position, velocity, shape)


class EarthEffect(Effect):
    def __init__(self, level):
        super().__init__(
            level,
            effect_type=EffectType.EARTH,
            setting_type=SettingType.WEIGHT,
            base_cost=1,
        )


class TimeEffect(Effect):
    def __init__(self, level):
        super().__init__(
            level,
            effect_type=EffectType.TIME,
            setting_type=SettingType.RATE,
            base_cost=10,
        )
