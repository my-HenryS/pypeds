from abc import ABC, abstractmethod

__all__ = ['Entity', 'Agent', 'Dummy']


class Entity(ABC):

    def __init__(self, shape):
        self.shape = shape
        self.model = None
        self.drawer = None
        self.name = None

    def move_to(self, pos):
        self.shape.move_to(pos)

    @abstractmethod
    def affect(self, agent):
        pass


class Agent(Entity):
    def __init__(self, shape):
        super(Agent, self).__init__(shape)

    def affect(self, agent):
        self.model.get_force(self, agent)


class Dummy(Entity):  # FIXME remove it after use
    def __init__(self, shape):
        super(Dummy, self).__init__(shape)

    def affect(self, agent):
        self.model.get_force(self, agent)

