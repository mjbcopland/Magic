from Props import *
from Elements import *
import inspect


class Tile:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.actions = []
        self.elements = []
        self.props = []
        self.speech_log = []
        self.state = {"Temperature": 24, "Time": 1, "Gravity": 9.81, "Fuel": False, "Conductor": False}

    def resolve_tile(self):
        self.action_phase()
        self.elements_phase()

    def speech_phase(self):
        self.speech_log =[]
        for prop in self.props:
            if isinstance(prop, Wizard):
                one_person_log = prop.return_speech()
                for speech in one_person_log:
                    self.speech_log.append(speech)
        return self.speech_log

    def action_phase(self):
        for action in self.actions:
            self.elements, self.props = action.act(self.elements, self.props)
        self.actions = []

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
        self.actions.append(action)

    def get_information(self):
        return str(self.coordinates) + " with world effects " + str(len(self.elements))
