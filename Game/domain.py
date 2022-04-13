import typing
from entity import Physical_Entity
from world import world


class Domain(Physical_Entity):
    """
    a domain is a large sort of enviroment, maybe a city, or a planet
    """
    def __init__(self, name='stock domain') -> None:
        Physical_Entity.__init__(self, name)
        self.connections = dict()
        world.domains[self.name] = self
    def enter(self):
        print(f'congratulations, you have entered {self.name}')
    def connect(self, sister):
        self.connections[sister.name] = sister
        sister.connections[self.name] = self


class Derelict(Domain):
    """
    the entire structure
    """
    def __init__(self) -> None:
        pass
class Ship_Hull(Domain):
    """
    
    """
    def __init__(self) -> None:
        pass

class Ship_Wing(Domain):
    """
    
    """
    def __init__(self) -> None:
        pass

class Room(Domain):
    """
    a type of domain that is artificial and can be occupied
    """
    
    def __init__(self, name='stock room') -> None:
        Domain.__init__(self,name)
        contents = {
        'in':[],
        'under':[],
        'above':[],
        }
        self.spatial_relations = contents.keys()
        self.local_names = dict()# changes dynamically