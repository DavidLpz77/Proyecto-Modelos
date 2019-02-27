class Aurora():
    nameaurora=None
    imageaurora=None
    def getNameAurora(self):
        return self.nameaurora
    
    def __init__(self):
        pass
    def showAurora(self):
        pass
    def getImageAurora(self):
        return self.imageaurora
    

class WaterAurora(Aurora):
    def __init__(self):
        self.nameaurora="Water Aurora"
        self.imageaurora="aurora\Aurora.png"
    def showAurora(self):
        pass
    
    
class FireAurora(Aurora):
    def __init__(self):
        self.nameaurora="Fire Aurora"
        self.imageaurora="aurora\Aurora1.png"
    def showAurora(self):
        pass
    
    
class DevilAurora(Aurora):
    def __init__(self):
        self.nameaurora="Devil Aurora"
        self.imageaurora="aurora\Aurora2.png"
    def showAurora(self):
        pass
    
class PsychicAurora(Aurora):
    def __init__(self):
        self.nameaurora="PsychicAurora"
        self.imageaurora="aurora\Aurora3.png"
    def showAurora(self):
        pass
    
