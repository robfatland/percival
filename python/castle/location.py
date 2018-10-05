class location(object):
    """A location is a place you can be in the course of running the adventure.
    Locations include states, descriptions, possible actions (that change states)
    and even suggestions for what to do."""
    state = [False, False, False, False, False]
    adjacent = []

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "The {}:\n{}\nStatus for debugging: {}\n".format(self.name, self.description, self.value)


class room(location):
    """A specific type of location that is room-like..."""






