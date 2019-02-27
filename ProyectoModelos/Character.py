'''
@author: David Lopez
'''
from copy import deepcopy


class Character():


    weapon=None
    objclone=None
    
    image=None
    aurora= None
    auroraNum=None

    
    def clone(self):
        return deepcopy(self)
    
    def __init__(self):
        pass
    def setWeapon(self, weapon):
        self.weapon=weapon
    def getWeapon(self):
        return self.weapon
    
    def getImage(self):
        return self.image
    def setAurora(self, aurora):
        self.auroraNum=aurora
        if (aurora==0):
            self.aurora="aurora/Aurora.png"

        if (aurora==1):
            self.aurora="aurora/Aurora1.png"

        if (aurora==2):
            self.aurora="aurora/Aurora2.png"

        if (aurora==3):
            self.aurora="aurora/Aurora3.png"

    def getAurora(self):
        return self.aurora
    def getAuroraNum(self):
        return self.auroraNum

   

    #metodo de prueba
    def hable(self):
        pass
    
class DevilConjurer(Character):
    def __init__(self):
        print("hola soy una bruja oscura")


class Conjurer(Character):

    def __init__(self, attack):
        self._Attack = attack
        print("hola soy una bruja buena")
        self.image = "imagenes/bruja.png"

    def attack(self):
        self._Attack.attack()

    # metodo de prueba
    def hable(self):
        return ("yo soy una bruja")


class Adapter(Conjurer):
    _devilConjurer=None
    def __init__(self, Conjurer, attack):
        self._Attack = attack
        self._devilConjurer=Conjurer

    def getImage(self):
        return "imagenes/bruja2.png"

    def attack(self):
        self._Attack.attack()
    
class Devil(Character):
    
    def __init__(self, attack):
        self._Attack = attack
        print("hola soy un demonio")
        self.image = "imagenes\Demonio.png"
        
    def attack(self):
        self._Attack.attack()

    #metodo de prueba
    def hable(self):
        return("yo soy demonio")
    
    
class Orc(Character):
    def __init__(self, attack):
        self._Attack = attack
        print("hola soy un orco")
        self.image = "imagenes\orco.png"

    def attack(self):
        self._Attack.attack()
        
    #metodo de prueba
    def hable(self):
        return("yo soy orco")
    
    
class Warrior(Character):
    def __init__(self, attack):
        self._Attack = attack
        print("hola soy un Enano")
        self.image = "imagenes\enano.png"

    def attack(self):
        self._Attack.attack()
        
        
    #metodo de prueba
    def hable(self):
        return("Yo soy un Enano Gerrero")
    
    
    
