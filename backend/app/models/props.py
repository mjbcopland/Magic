from django.db import models


class Props(models.Model):
    class Meta:
        abstract = True

    health = models.IntegerField(default=1)
    mana = models.IntegerField(default=1)


class Wizard(Props):
    health = models.IntegerField(default=100)
    mana = models.IntegerField(default=100)


class PropsObject:
    def __init__(self, position, velocity, health=1, mana=1):
        self.position = position
        self.velocity = velocity
        self.health = health
        self.mana = mana


class WizardObject(Props):
    def __init__(self, position, velocity):
        super().__init__(position, velocity, health=100, mana=100)

    def shout(self, string):
        return Spell(string).decode_incantation(self.position).cast()
