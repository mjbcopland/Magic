from Props import *
from Spell import *
import inspect


class Tile:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.actions = []
        self.elements = []
        self.props = []
        self.state = {"Temperature": 24, "Time": 1, "Gravity": 9.81, "Fuel": False, "Conductor": False}

    def resolve_tile(self):
#        self.elements_phase(self)
        pass

    def spell_phase(self):
        for prop in self.props:
            if inspect.isinstance(prop, Wizard):
                speech_log = prop.return_speech()
                spell = Spell(speech_log)
                spell = spell.decode_incantation(self.coordinates)
                spell.cast()

    def action_phase(self):
        for action in self.actions:
            print('foo')

    def elements_phase(self):
        self.state['Fuel'] = False
        self.state['Conductor'] = False

        for element in self.elements:
            self.state = element.interact_on(self.state)
        for objects_index, element in enumerate(self.elements):
            self.elements[objects_index] = element.interact_from(self.state)

        self.elements = list(filter(None, self.elements))

    def props_phase(self):
        for prop in self.props:
            print('foo')

    def add_actions(self, action):
        print("Added one action")
        self.actions.append(action)

    def get_information(self):
        return str(self.coordinates) + " with world effects " + str(len(self.elements))
