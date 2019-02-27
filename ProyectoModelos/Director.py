'''
@author: David Lopez
'''
class Director():
    constructor=None
    def __init__(self):
        pass
    def setBuilder(self, constructor):
        self.constructor=constructor
    def getCharacter(self):
        return self.constructor.getCharacter()
    def BuildCharacter(self, character, weapon, aurora):
        self.constructor.buildCharacter(character)
        self.constructor.buildWeapon(weapon)
        self.constructor.buildAurora(aurora)
