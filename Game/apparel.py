
from object import Prop

class Apparel(Prop):
    """
    anything that can be worn
    """
    def __init__(self, name) -> None:
        self.name = name