from AuroraCreator import WaterAuroraCreator
from AuroraCreator import FireAuroraCreator
from AuroraCreator import DevilAuroraCreator
from AuroraCreator import PsychicAuroraCreator

class DetermineAurora():
    def __init__(self):
        pass
    createaurora=None
    aurora=None
    def createAurora(self, number):
        self.createaurora={1: WaterAuroraCreator(), 2: FireAuroraCreator(), 3: DevilAuroraCreator(), 4: PsychicAuroraCreator() }
    def getAurora(self):
        return self.aurora