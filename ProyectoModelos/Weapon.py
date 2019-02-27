'''
@author: David Lopez
'''

class Weapon():
    nameweapon=None
    imageweapon=None
    def getNameWeapon(self):
        return self.nameweapon
    
    def __init__(self):
        pass
    def showWeapon(self):
        pass
    def getImageWeapon(self):
        return self.imageweapon
    

class VampireSpear(Weapon):
    def __init__(self):
        self.nameweapon="Vampire Spear"
        self.imageweapon="imagenes\VampireSpear.png"
    def showWeapon(self):
        pass
    
    
class OdinSpear(Weapon):
    def __init__(self):
        self.nameweapon="Odin Spear"
        self.imageweapon="imagenes\OdinSpear.png"
    def showWeapon(self):
        pass
    
    
class MortalDagger(Weapon):
    def __init__(self):
        self.nameweapon="Mortal Dagger"
        self.imageweapon="imagenes\MortalDagger.png"
    def showWeapon(self):
        pass
    
class LegendaryCane(Weapon):
    def __init__(self):
        self.nameweapon="Legendary Cane"
        self.imageweapon="imagenes\Scepter.png"
    def showWeapon(self):
        pass
    
class HeavenlyScepter(Weapon):
    def __init__(self):
        self.nameweapon="Heavenly Scepter"
        self.imageweapon="imagenes\HeavenlyScepter.png"
    def showWeapon(self):
        pass
    
class HadesSword(Weapon):
    def __init__(self):
        self.nameweapon="Hades Sword"
        self.imageweapon="imagenes\HadesSword.png"
    def showWeapon(self):
        pass

class ExcaliburSword(Weapon):
    def __init__(self):
        self.nameweapon="Excalibur Sword"
        self.imageweapon="imagenes\ExcaliburSword.png"
    def showWeapon(self):
        pass
    
class EpicScepter(Weapon):
    def __init__(self):
        self.nameweapon = "Epic Scepter"
        self.imageweapon = "imagenes\EpicScepter.png"
    def showWeapon(self):
        pass
    
class DragonTail(Weapon):
    def __init__(self):
        self.nameweapon="Dragon Tail"
        self.imageweapon="imagenes\DragonTail.png"
    def showWeapon(self):
        pass
    
class DragonSword(Weapon):
    def __init__(self):
        self.nameweapon="Dragon Sword"
        self.imageweapon="imagenes\Hammer.png"
        
    def showWeapon(self):
        pass
    
class DemonSword(Weapon):
    def __init__(self):
        self.nameweapon="Demon Sword"
        self.imageweapon="imagenes\DragonHammer.png"
        
    def showWeapon(self):
        pass
    
class DamnBlade(Weapon):
    def __init__(self):
        self.nameweapon="Damn Blade"
        self.imageweapon="imagenes\DamnBlade.png"
        
    def showWeapon(self):
        pass
