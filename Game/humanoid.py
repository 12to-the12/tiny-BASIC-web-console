
from character import Physical_Character
from character import NPC
from utilities import eval_boolean
from world import world



class Humanoid(Physical_Character):
    """
    any character that has a similar body plan to a human, a cyborg, an enhanced human, or contemporary humans
    """
    def __init__(self, name='humanoid', max_weight=20) -> None:
        Physical_Character.__init__(self, name=name)
        # verb aliases and their corresponding methods
        # this is used to map different synonyms to their corresponding methods
        # these methods are accessible to the player
        # technically each instance doens't need their own copy, but this is easier to implement
        # accessed by the perform method
        self.actionalias_table: list = [
            [ ['move', 'walk'], self.move ],
            [ ['hallo', 'hullo'], self.equip ]
        ]
        self.actions = list()

        for pairing in self.actionalias_table:
            aliases: list = pairing[0]
            method = pairing[1]
            self.actions.extend(aliases) 

        
        # these are the pieces of clothing or accessories at these particular locations
        self.apparel = {
            'head':None,
            'neck':None,
            'clothing':None,
            'wrists':None,
        }

        active = None # held in the dominant hand
        
        self.inventory = []
        self.burden = 0 # the amount of weight the human is carrying
        self.max_weight = max_weight # kilos
    
    def perform(self, action, body):# all the player accessible methods
        for aliases, methods in self.actionalias_table:
            if action in aliases:
                print(f"body:{body}")
                try: return methods(body)
                except Exception as ex: raise Exception(ex)
        raise Exception(f"{self} can't {action}")

    def add_inventory(self, object) -> None:
        if  object.weight > ( self.max_weight - self.burden ):
            raise Exception(f"{self.name} can't carry more than their max weight of {self.max_weight} kilos, you monster tried to burden them with {object.weight}")
        else:
            self.inventory.append(object)
            self.burden += object.weight

    def remove_inventory(self, object) -> None:
        if  object in self.inventory:
            self.inventory.remove( object )
        else:
            raise Exception(f"that object isn't in the inventory of {self.name}")
    
    def equip(self, item) -> None:# equips new apparel, stashes the thing already there if it can, prompts player to discard it if it can't
        if self.apparel[ item.slot ] != None:# if theres already something in the slot
            try:# try to put the thing already there in inventory
                self.add_inventory( self.apparel[ item.slot ] )
                print('equipped')
            except:
                print('you can\'t carry the thing already equipped there, discard it instead?')
                if eval_boolean( input('>>>') ): # if the player wants to discard the current thing in the slot, discard it then equip the new thing
                    self.discard( self.apparel[ item.slot ] )
                    self.apparel[ item.slot ] = item
                else:
                    pass
    def change_location(self, new_location):
        if new_location in self.active_domain.connections.keys():
            self.active_domain = new_location
        else: raise Exception("can\'t go to {new_location}")

    def move(self, body):
        print(self.active_domain.connections.keys())
        print(world.domains.keys())
        print(f"body{body}")
        target, *body = body
        print(target)
        if target == []:
            raise Exception('where?')
        connections = self.active_domain.connections.keys()
        if target in world.domains.keys():# if space exists
            try: self.change_location(target)
            except: raise Exception("You can't access {target} from where you are") 
            else: return f"you are now at {target}"
        else: raise Exception("that location doens't exist")


class Human(Humanoid):
    """
    contemporary humans
    """
    def __init__(self, name='hooman') -> None:
        Humanoid.__init__(self, name=name)

        
class  Modified_Human(Humanoid):
    """
    any sort of genetically modified human
    """
    def __init__(self) -> None:
        Humanoid.__init__(self)

class  Cyborg(Humanoid):
    """
    a human that's been heavily modifed with mechanical parts
    """
    def __init__(self) -> None:
        Humanoid.__init__(self)


class Player_Character(Human):
    """
    the place for the attributes and abilities of the player character
    """
    def __init__(self, name='player character') -> None:
        Human.__init__(self, name=name)


class Human_NPC(Human, NPC):
    """
    human non player character
    """
    def __init__(self) -> None:
        pass