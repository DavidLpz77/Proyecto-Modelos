'''
@author: David Lopez
'''

from DetermineCharacter import DetermineCharacter
from DetermineWeapon import DetermineWeapon
from Director import Director
from Builder import CharacterBuilder
from random import *
from Character import *


class EnlistCharacter:
    personajesclonados = None

    determinarpersonaje = None
    determinararma = None
    determinarAurora = None
    constructorpersonaje = None
    armarpersonaje = None

    def __init__(self):
        self.determinarpersonaje = DetermineCharacter()
        self.determinararma = DetermineWeapon()
        self.determinaraurora = Character()
        self.constructorpersonaje = CharacterBuilder()
        self.armarpersonaje = Director()

    def generateChackra(func):
        x = randint(0, 3)
        def wrapper(self):
            func(self, x)
            return func
        return wrapper

    def createWeapon(self, number):
        self.determinararma.createWeapon(number)

    @generateChackra                #decorador
    def createAurora(self, number):
        print(str(number))
        self.determinaraurora.setAurora(number)


    def createCharacter(self, number):
        self.determinarpersonaje.createCharacter(number)

    def BuildCharacter(self):
        self.armarpersonaje.setBuilder(self.constructorpersonaje)
        self.armarpersonaje.BuildCharacter(self.determinarpersonaje.getCharacter(), self.determinararma.getWeapon(), self.determinaraurora.getAuroraNum())

    def cloneCharacter(self):
        self.personajesclonados = self.armarpersonaje.getCharacter()
        return self.personajesclonados.clone()
