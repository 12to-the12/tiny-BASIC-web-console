import typing
import domain
from world import world
from humanoid import Player_Character

derelict = domain.Derelict()

origin = domain.Room(name='origin')
sister = domain.Room(name='sister')
origin.connect(sister)
player = Player_Character(name="the player")
player.active_domain = origin
print('set active domain')

world.structure = origin
















def help():
    return """Useful commands:
 
   The 'BRIEF' command suppresses printing of long room descriptions for rooms which have been visited.  The 'SUPERBRIEF' command suppresses printing of long room descriptions for all rooms.  The 'VERBOSE' command restores long descriptions. 
   The 'INFO' command prints information which might give some idea of what the game is about. 
   The 'QUIT' command prints your score and asks whether you wish to continue playing. 
   The 'SAVE' command saves the state of the game for later continuation. 
   The 'RESTORE' command restores a saved game. 
   The 'INVENTORY' command lists the objects in your possession. 
   The 'LOOK' command prints a description of your surroundings. 
   The 'SCORE' command prints your current score and ranking. 
   The 'TIME' command tells you how long you have been playing. 
   The 'DIAGNOSE' command reports on your injuries, if any.
 
Command abbreviations:
 
   The 'INVENTORY' command may be abbreviated 'I'. 
   The 'LOOK' command may be abbreviated 'L'. 
   The 'QUIT' command may be abbreviated 'Q'.
 
Containment:
 
   Some objects can contain other objects.  Many such containers can be opened and closed.  The rest are always open.   They may or may not be transparent.  For you to access (e.g., take) an object which is in a container, the container must be open.  For you to see such an object, the container must be either open or transparent.  Containers have a capacity, and objects have sizes; the number of objects which will fit therefore depends on their sizes.  You may put any object you have access to (it need not be in your hands) into any other object.  At some point, the program will attempt to pick it up if you don't already have it, which process may fail if you're carrying too much.  Although containers can contain other containers, the program doesn't access more than one level down.
 
Fighting:
 
   Occupants of the dungeon will, as a rule, fight back when attacked.  In some cases, they may attack even if unprovoked. Useful verbs here are 'ATTACK <villain> WITH <weapon>', 'KILL', etc.  Knife-throwing may or may not be useful.  You have a fighting strength which varies with time.  Being in a fight, getting killed, and being injured all lower this strength. Strength is regained with time.  Thus, it is not a good idea to fight someone immediately after being killed.  Other details should become apparent after a few melees or deaths.
 
Command parser:
 
   A command is one line of text terminated by a carriage return. For reasons of simplicity, all words are distinguished by their first nine letters.  All others are ignored.  For example, typing 'DISASSEMBLE THE ENCYCLOPEDIA' is not only meaningless, it also creates excess effort for your fingers.  Note that this truncation may produce ambiguities in the interpretation of longer words.
 
   You are dealing with a fairly stupid parser, which understands the following types of things--
 
   Actions: 
        Among the more obvious of these, such as TAKE, PUT, DROP, etc. 
        Fairly general forms of these may be used, such as PICK UP, 
        PUT DOWN, etc.
 
   Directions: 
        NORTH, SOUTH, UP, DOWN, etc. and their various abbreviations. 
        Other more obscure directions (LAND, CROSS) are appropriate in 
        only certain situations.
 
   Objects: 
        Most objects have names and can be referenced by them.
 
   Adjectives: 
        Some adjectives are understood and required when there are 
        two objects which can be referenced with the same 'name' (e.g., 
        DOORs, BUTTONs).
 
   Prepositions: 
        It may be necessary in some cases to include prepositions, but 
        the parser attempts to handle cases which aren't ambiguous 
        without.  Thus 'GIVE CAR TO DEMON' will work, as will 'GIVE DEMON 
        CAR'.  'GIVE CAR DEMON' probably won't do anything interesting. 
        When a preposition is used, it should be appropriate;  'GIVE CAR 
        WITH DEMON' won't parse.
 
   Sentences: 
        The parser understands a reasonable number of syntactic construc- 
        tions.  In particular, multiple commands (separated by commas) 
        can be placed on the same line.
 
   Ambiguity: 
        The parser tries to be clever about what to do in the case of 
        actions which require objects that are not explicitly specified. 
        If there is only one possible object, the parser will assume 
        that it should be used.  Otherwise, the parser will ask. 
        Most questions asked by the parser can be answered."""

def run(*args):
    line = ''.join(*args)
    try: return exec(line)
    except: raise Exception("Error")
        
def location():
     return player.active_domain.name
     
world.command_table = {
    'help':help,
    'exec':run,
    'python':run,
    'execute':run,
    'code':run,
    'location':location
}
    




