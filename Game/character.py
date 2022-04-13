import typing
import random
#from gpt3 import query
from entity import Physical_Entity


class Character(Physical_Entity):
    """
    any sort of being that exists within the world
    """
    def __init__(self, name='John Cena') -> None:
        Physical_Entity.__init__(self, name)


class Physical_Character(Character):
    """
    any character that exists within physical and has a body
    """
    def __init__(self, name='bolts') -> None:
        Character.__init__(self,  name=name)
        self.domain_stack = []
        self.active_domain = None
    def set_active_domain(self, active):
        if active in self.active_domain.connections:
            self.active_domain = active
            active.enter()
        else:
            raise Exception(f"that domain doesn't connect to {self.name}'s current domain")

class AI(Character):
    """
    a variety of character that doesn't have a physical being
    """
    def __init__(self, name='Hal 1000') -> None:
        Character.__init__(self, name)

class NPC(Character):
    """
    non player character
    """
    def __init__(self, name='Jonathan Webster') -> None:
        Character.__init__(self, name)



class Free_Guy(Character):
    """
    complex non player character
    """
    
    def __init__(self, name='an NPC', identity=False) -> None:
        Character.__init__(self, name)
        self.identity = identity
        if not self.identity:# if no identity is specified
            self.identity = f"my name is {self.name}, I've been living on a derelict spaceship left to rot in the void for 22 years now. If you ask me a question thats insulting I'll insult you back. \
            if you ask a question I know the answer to I'll answer, but only if you are respectful. I live in a small colony with a handful of other people in a settlement that's been in place for 500 standard earth years. \
            Everyday is filled with difficult work maintaining the power core the community is built around, but if it means I get to live another day with my loving wife and children, It's worth it, \
            \n\n>>> Excuse me, can you tell me what happened to this place?\n{self.name}: \
            We were hit by a famine a couple years ago, people haven't been the same since.\n\n>>> That's horrible, I'm so sorry. Would you mind pointing me towards the nearest macchine shop, I need to fix my carrier drone?\n{self.name}: \
            Down the north corridor, third door on the left.\n\n>>> Thanks, oh, and what's deal with your face? \
            \n{self.name}: Fuck off and go bother some other poor soul.\n\n>>> Right, I'm sorry, that was uncalled for. You guys deserve better, thanklessly maintaining the power core for decades. \
            \n{self.name}: Centuries, actually"
        else: self.identity = identity

    def converse(self):
        conversing = True
        print(f'talking to {self.name}, enter "quit" at anytime to end the conversation')
        accumulator = self.identity
        while conversing:
            print()
            player_sentence = input('>>>')
            if player_sentence.strip() == 'quit':
                conversing = False
            
            accumulator = accumulator + '\n\n>>> ' + player_sentence + f'\n{self.name}: '# adds the player's sentence to the text seen by the ai
            NPC_sentence = query(prompt=accumulator)
            NPC_sentence.strip()
            print(NPC_sentence)
            accumulator = accumulator + NPC_sentence