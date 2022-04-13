

import typing
from verbs import verbs
from quips import quips
from world import world
from initialize import player
#from wordlists import word_lists







class Noun_Phrase():
    """
    a noun phrase is the part of a sentence that expounds upon the noun
    "the large blue butterfly" is a noun phrase
    they consist of articles, adjectives, and of course nouns
    """
    def __init__(self, subject) -> None:
        subject = subject

class Parser():
    """
    an object that turns natural language into a structured representation of it's meaning
    the structured representation consists of a dictionary with the part of speech as the key
    and an object as the value
    accepted types:
        prepositional phrase ( contains the spatiality and the object )
        noun phrase ( not an object type, refers to the object itself )
        verb
    """
    pronouns = {
        'him':None,
        'her':None,
        'them':None,
        'it':None
    }
    def parse(command):
        """
        attempts to execute the command given by the player
        the first pass is quips
        then unviersal commands
        then player actions,
        where local names take precedence
        over global names """
        local_names = player.active_domain.local_names
        
        # first pass is quips
        if command in quips.keys():
            print('that is recognized as a quip')
            return quips[command]
        words = command.split()

        
        verb, *body = words # the first goes to verb everything else goes to body
        
        
        # second is control commands
        #print(world.command_table.keys())
        print(verb)
        if verb in world.command_table.keys():
            print('that is recognized as a world command')
            try:# only tested for legitimacy if it's a command
                print('running the command')
                return world.command_table[verb](body)
            except Exception as ex:# if the command fails
                raise Exception(ex)

        # depreciated because it was annoying to implement
        """
        # this allows you to intentionally break things
        force = False
        if verb=='force': verb, *body = body
        """
        
        if verb in player.actions:# if it's something the player can do
            print('that is recognized as a player action')
            print(f"body:{body}")
            # if the first word of the command is a control, execute the associated function with the remaining values
            try: return player.perform(verb, body)# if body isn't empty
            except Exception as ex:
                raise Exception(f"can't perform that action because {ex}")
                
        #sanitize()
        elif verb not in player.actions:
            if verb in verbs: # if the word is a recognized verb
                raise Exception(f"that's not something {player.name} can do")
            else:
                return 'enter an actual command'# this is not an error
        else:
            return "I am confused as to how this was triggered"

        
        
        #identify_POS() # identify part of speech

        print(words)
        # replace with local name spaces
    
    def sanitize(self):
        # outdated
        '''
        if all([word in Parser.vocabulary or local_names.keys() for word in words]):
            print("they're all accepted")
        else:
            print(" some of the words in the command aren't recognized")
        '''
        # discards articles from word list
        articles = ['the','a','an']
        words = list( filter( lambda x: x not in articles,  words) )

    def identify_POS(self): # part of speech not piece of shit
        POS = []
        for word in words:
            if word in word_lists['verbs']:
                POS.append(  ('verb', word)   )
            elif word in word_lists['prepositions']:
                POS.append(  ('preposition', word)   )
            else:
                POS.append(  (None, word)   )
        find_local()
        
        
        
        
        identify_local()# finds local names and builds out list based on them

    def verify(self):
        pass



if __name__ == "__main__":
    clear()
    # prepositions can act upon either nouns or verbs
    # stare at the cabin by the lake
    # catch the ball with the glove
    command = 'walk forwards'# the method walk of thhe player class is invoked, with the argument forward
    command = 'draw a face on the chalkboard'# invokes the draw method of the player, with the argument face for the subject, and chalkboard for the location
    command = 'shoot the castle guard'# invokes the player's shoot method with thw subject as castleguard and the location defaulting to chest
    command = 'throw the cat over it'
    command = 'run quickly towards the green banana'
    # you can't run quickly, but the banana IS green, you need to be able to differentiate between bananas!
    # adverbs aren't important but adjectives are
    command = 'shoot the alien with the large green machine gun in the chest'
    local_names = {'alien':None, 'large green machine gun':None}
    tree = Parser(command, local_names)