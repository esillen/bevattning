class Valve:
    def __init__(self, index, state = False, flow = 0.0):
        self.index = index
        self.state = bool(state)
        self.flow = flow

    def __str__(self):
        return "Valve with index: " + str(self.index) + " state: " + str(self.state)