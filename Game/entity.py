import typing

class Physical_Entity:
    """
    the parent class for anything that exists in the game world


    any object that exists in the game world

    the args allow you to specify the allowed spatial relationships

    the kwargs allow you to specify the things in those places
    
    """
    registry = dict()
    def __init__(self, name='entity', *args, **kwargs) -> None:
        Physical_Entity.registry[name] = self
        self.name = name

        self.spatial_relations = {
            'above':None,
            'across':None,
            'against':None,
            'among':None,
            'around':None,
            'at':None,
            'before':None,
            'behind':None,
            'below':None,
            'beside':None,
            'between':None,
            'by':None,
            'dow':None,
            'in':None,
            'inside':None,
            'near':None,
            'on':None,
            'over':None,
            'through':None,
            'under':None,
            'up':None,
            'beneath':None
        }

        # this defines a spatial relationship for every argument
        for relation in args:
            self.spatial_relations[relation] = []


        # this puts things  at the locations specified, allows single items or lists of items
        for relation, thing in kwargs.items():
            if relation in self.spatial_relations.keys():
                if type(thing)==list: self.spatial_relations[relation].extend(thing)
                else: self.spatial_relations[relation].append(thing)
            else:
                raise Exception(f'you can\'t put things {relation} a {self.__name__} silly')

    def allow(self, relation):# defines a spatial relation for this object
        if self.spatial_relations[relation] == None:
            self.spatiial_relation[relation] = []
        else:
            raise Exception('you cannot add a spatial relation if it\'s already defined')
    def add(self, relation:str, thing): # put a thing at this object in the relations
        try:
            self.spatial_relations[relation].append(thing)
        except:
            raise Exception(f'you can\'t go {relation} this object')
    def __str__(self):
        return self.name
    def __repr__(self):
        return f'(a {self.__class__.__name__} called {self.name})'