class Valve:
    def __init__(self, index, state = False):
        self.index = index
        self.state = bool(state)

    def __str__(self):
        return "Valve with index: " + str(self.index) + " state: " + str(self.state)

    def __dict__(self):
        return {'index':self.index, 'state':self.state}