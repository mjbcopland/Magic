class Tile:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.elements = []
        self.state = {"Temperature": 24, "Time": 1, "Gravity": 9.81, "Fuel": False, "Conductor": False}

    def resolve_tile(self):
        self.state['Fuel'] = False
        self.state['Conductor'] = False

        for element in self.elements:
            self.state = element.interact_on(self.state)
        for objects_index, element in enumerate(self.elements):
            self.elements[objects_index] = element.interact_from(self.state)

        self.elements = list(filter(None, self.elements))


    def add_object(self, object):
        self.elements.append(object)

    def get_information(self):
        return str(self.coordinates) + " with world effects " + str(len(self.elements))
