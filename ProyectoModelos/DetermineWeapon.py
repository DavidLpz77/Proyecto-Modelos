'''
@author: David Lopez
'''
from WeaponCreator import EpicScepterCreator
from WeaponCreator import LegendaryCaneCreator
from WeaponCreator import HeavenlyScepterCreator
from WeaponCreator import DamnBladeCreator
from WeaponCreator import HadesSwordCreator
from WeaponCreator import DemonSwordCreator
from WeaponCreator import DragonSwordCreator
from WeaponCreator import OdinSpearCreator
from WeaponCreator import ExcaliburSwordCreator
from WeaponCreator import MortalDaggerCreator
from WeaponCreator import VampireSpearCreator
from WeaponCreator import DragonTailCreator
class DetermineWeapon():
    def __init__(self):
        pass
    createweapon=None
    weapon=None
    def createWeapon(self, number):
        self.createweapon={1: EpicScepterCreator(), 2: HeavenlyScepterCreator(), 3: LegendaryCaneCreator(), 4: HadesSwordCreator(),
                   5: DamnBladeCreator(), 6: DemonSwordCreator(), 7: ExcaliburSwordCreator(), 8: DragonSwordCreator(),
                   9: OdinSpearCreator(), 10: DragonTailCreator(), 11: MortalDaggerCreator(), 12: VampireSpearCreator() }
        self.weapon = self.createweapon[number].CreateWeapon()
        print(str(self.weapon))
    def getWeapon(self):
        return self.weapon
    
    
    
    
