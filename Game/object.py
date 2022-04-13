from typing import overload
from entity import Physical_Entity

class Object(Physical_Entity):
    """
    any object that exists in the game world

    the args allow you to specify the allowed spatial relationships

    the kwargs allow you to specify the things in those places
    """
    def __init__(self, name='object', hidden=False, *args, **kwargs) -> None:
        Physical_Entity.__init__(self, name, *args, **kwargs)
        self.name = name
        self.hidden = hidden




class Prop(Object):
    """
    any object that can be manipulated
    """
    def __init__(self, name, weight=float('inf')) -> None:
        Object.__init__(self, name)
        self.weight = weight