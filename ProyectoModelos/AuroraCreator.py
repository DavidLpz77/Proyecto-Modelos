from Aurora import WaterAurora
from Aurora import FireAurora
from Aurora import DevilAurora
from Aurora import PsychicAurora



class AuroraCreator():
    def __init__(self):
        pass
    def CreateAurora(self):
        return self.factorymethod()
    def factorymethod(self):
        pass
    
    
class WaterAuroraCreator(AuroraCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return WaterAurora()
    

class FireAuroraCreator(AuroraCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return FireAurora()
    
class DevilAuroraCreator(AuroraCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return DevilAurora()
    

class PsychicAuroraCreator(AuroraCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return PsychicAurora()
    

    