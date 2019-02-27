'''
@author: David Lopez
'''
from Character import Conjurer
from Character import Devil
from Character import Orc
from Character import Warrior
from Character import Adapter


class Strategy():
    damage = 10

    def __init__(self,func=None):
        if func:
             self.attack = func

    def attack(self):
        print("Attacking with " + str(self.damage) + " hit points")


class AttackA(Strategy):

    def attackA():
        print("Attacking with " + str(Strategy.damage+10) + " hit points")


class AttackB(Strategy):

    def attackB():
        damage=Strategy.damage
        print("Attacking with " + str(damage + 5) + " hit points")


class CharacterCreator():
    def __init__(self):
        pass
    def factorymethod(self):
        pass
    def CreateCharacter(self):
        return self.factorymethod()


class ConjurerCreator(CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return Conjurer(Strategy())


class EvilConjurerCreator(CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        x = Conjurer(Strategy())
        evilConjurer = Adapter(x, Strategy(AttackA.attackA))
        return evilConjurer


class DevilCreator(CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return Devil(Strategy(AttackA.attackA))


class OrcCreator(CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return Orc(Strategy(AttackB.attackB))


class WarriorCreator(CharacterCreator):
    def __init__(self):
        pass
    def factorymethod(self):
        return Warrior(Strategy(AttackB.attackB))
