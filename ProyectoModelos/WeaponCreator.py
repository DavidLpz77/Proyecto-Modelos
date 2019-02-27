'''
@author: David Lopez
'''
from Weapon import VampireSpear
from Weapon import OdinSpear
from Weapon import MortalDagger
from Weapon import LegendaryCane
from Weapon import HeavenlyScepter
from Weapon import HadesSword
from Weapon import ExcaliburSword
from Weapon import EpicScepter
from Weapon import DragonTail
from Weapon import DragonSword
from Weapon import DemonSword
from Weapon import  DamnBlade 


class WeaponCreator():
    def __init__(self):
        pass
    def CreateWeapon(self):
        return self.factorymethod()
    def factorymethod(self):
        pass
    
    
class VampireSpearCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return VampireSpear()
    

class OdinSpearCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return OdinSpear()
    
class MortalDaggerCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return MortalDagger()
    

class LegendaryCaneCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return LegendaryCane()
    
    
class HeavenlyScepterCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return HeavenlyScepter()
    

class HadesSwordCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return HadesSword()
    
    
class ExcaliburSwordCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return ExcaliburSword()
    
    
class EpicScepterCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return EpicScepter()
    
    
class DragonTailCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return DragonTail()
    
    
class DragonSwordCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return DragonSword()
    
    
class DemonSwordCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return DemonSword()
    
    
class DamnBladeCreator(WeaponCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return DamnBlade()
    
    
    
