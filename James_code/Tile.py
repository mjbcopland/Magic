class Tile:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.objects = []
        self.state = {"Temperature": 24, "Time": 1, "Gravity": 9.81, "Fuel": False, "Conductor": False}

    def resolve_tile(self):
        self.state['Fuel'] = False
        self.state['Conductor'] = False

        for object in self.objects:
            self.state = object.interact_on(self.state)
        for objects_index, object in enumerate(self.objects):
            self.objects[objects_index] = object.interact_from(self.state)

        self.objects = list(filter(None, self.objects))


    def add_object(self, object):
        self.objects.append(object)

    def get_information(self):
        return str(self.coordinates) + " with world effects " + str(len(self.objects))
