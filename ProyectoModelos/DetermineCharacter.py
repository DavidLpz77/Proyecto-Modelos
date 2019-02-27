'''
@author: David Lopez
'''
from CharacterCreator import *

class Handler():
    def __init__(self):
        pass
    succesor=None
    def handlerRequest(self, number):
        pass
    def getSuccesor(self):
        return self.succesor
    def setSuccesor(self, succeso):
        self.succesor = succeso

class HandlerOptDefault(Handler):
    def __init__(self):
        pass
    def handlerRequest(self, number):
        return CharacterCreator()
    
class HandlerOptOne(Handler):
    def __init__(self):
        pass
    def handlerRequest(self, number):
        if(number==1):
            return ConjurerCreator()
        else:
            return self.succesor.handlerRequest(number)

class HandlerOptTwo(Handler):
    def __init__(self):
        pass
    def handlerRequest(self, number):
        if(number==2):
            return DevilCreator()
        else:
            return self.succesor.handlerRequest(number)
        
    
class HandlerOptThree(Handler):
    def __init__(self):
        pass
    def handlerRequest(self, number):
        if(number==3):
            return WarriorCreator()
        else:
            return self.succesor.handlerRequest(number)
        

class HandlerOptFour(Handler):
    def __init__(self):
        pass
    def handlerRequest(self, number):
        if(number==4):
            return OrcCreator()
        else:
            return self.succesor.handlerRequest(number)


class HandlerOptFive(Handler):
    def __init__(self):
        pass

    def handlerRequest(self, number):
        if(number==5):
            return EvilConjurerCreator()
        else:
            return self.succesor.handlerRequest(number)
        
    
    
class DetermineCharacter():
    def __init__(self):
        pass
    createcharacter=None
    character=None
    handlers = [HandlerOptOne(), HandlerOptTwo(), HandlerOptThree(), HandlerOptFour(), HandlerOptFive(), HandlerOptDefault()]
    
    
    def createCharacter(self,number):
        
        for i in range(0 , len(self.handlers)-1 , 1):
            self.handlers[i].setSuccesor(self.handlers[i+1])
        
        self.createcharacter=self.handlers[0].handlerRequest(number)

        self.character=self.createcharacter.CreateCharacter()
        
    def getCharacter(self):
        return self.character
    

        
    
        
    
