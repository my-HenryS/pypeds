from abc import ABC, abstractmethod


class Entity(ABC):

    def __init__(self, shape):
        self.shape = shape
        self._model = None
        self.drawer = None
        self.name = None

    def move_to(self, pos):
        self.shape.center = pos

    @abstractmethod
    def affected(self, affection):
        pass

    @property
    @abstractmethod
    def view(self):
        pass

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    def distance(self, other):
        return self.shape.distance(other.shape)

class Blockable:
    pass


class Movable(Entity):

    def __init__(self, shape,):
        super(Movable, self).__init__(shape)
        self.velocity = None
        self.acc = None
        self.mass = None

    def affected(self, affection):
        if affection.a_type == "Force":
            force = affection.value
            self.acc = force / self.mass
            self.velocity += self.acc * self.model.time_per_step
            self.shape.center += self.velocity * self.model.time_per_step

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model
        self.velocity = model.zero_velocity()
        self.acc = model.zero_velocity()

    @property
    def view(self):
        return self.shape.get_expand(3)     # FIXME set abstract property view_range and remove hard code


class Agent(Movable, Blockable):
    def __init__(self, shape):
        super().__init__(shape)
        self.path = None

    def next_step(self):
        return self.path.next_step()

