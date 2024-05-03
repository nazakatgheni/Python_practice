class Player:
    # dunder method-double underscore
    # strength is 
    def __init__(self, name, strength = 100 ):
        
        self.name = name
        self.strength = strength

        self.weapons = []
        
    def walk(self):
        self.strength -= 1
        return self.strength