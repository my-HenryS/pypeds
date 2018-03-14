from abc import ABC, abstractmethod


class Entity(ABC):

    def __init__(self, shape):
        self.shape = shape
        self._model = None
        self.drawer = None
        self.name = None

    @abstractmethod
    def affected(self, affection):
        pass

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    def distance(self, other):
        return self.shape.distance(other.shape)

    @property
    def position(self):
        return self.shape.center

    @position.setter
    def position(self, pos):
        self.shape.center = pos


class Goal(Entity):
    def __init__(self, shape):
        super().__init__(shape)
        self.recorder = []

    def affected(self, affection):
        if affection.a_type == "Record":
            self.recorder.append(affection.value)


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
            self.position += self.velocity * self.model.time_per_step

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model
        self.velocity = model.zero_velocity()
        self.acc = model.zero_velocity()


class Escapable(Movable):

    def __init__(self, shape):
        super().__init__(shape)
        self.escaped = False

    def affected(self, affection):
        super().affected(affection)
        if affection.a_type == "Escape":
            self.escaped = affection.value


class Agent(Escapable):
    def __init__(self, shape):
        super().__init__(shape)
        self.path = None

    def next_step(self):
        return self.path.next_step(self.position)

