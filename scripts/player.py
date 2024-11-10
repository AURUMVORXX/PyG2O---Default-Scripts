import g2o

class Player:
    def __init__(self):
        self.sprintEnabled = False
        
    def clear(self):
        self.sprintEnabled = False
        
    def toggleSprint(self):
        self.sprintEnabled = not self.sprintEnabled