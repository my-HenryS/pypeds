from pypeds.pool import EntityPool
from pypeds.entity import Entity
from abc import ABC, abstractmethod
from threading import Thread
from pypeds.shape2d import *


class Scene(Thread):

    def __init__(self, model=None, strategy=None, pedestrain_shape=Circle2D):
        """ Define operations to the variable 'entities'.
        We here define a entities pool and restrict modifying it only with functions
        add_entity() and remove_entity(). We use EntityPool.get() to get a proportion of entities of a specific type.

        """
        super().__init__()
        self._entities = EntityPool()
        self.model = model
        self.time_step = 0
        self._listeners = []
        self.drawer = None
        self.strategy = strategy
        self.pedestrain_shape = pedestrain_shape

    @property
    def entities(self):
        return self._entities.select_by_type(Entity)
    """
    Add and remove entity
    
    """
    def add_entity(self, new_entity):
        self._entities.add(new_entity)
        new_entity.model = self.model

    def remove_entity(self, entity):
        self._entities.remove(entity)

    def entities_of_type(self, q_type: object) -> object:
        """
        :param: q_type: the query type
        :return: iterator that contains all required entities
        """
        return self._entities.select_by_type(q_type)

    def entities_in_region(self, region) -> iter:
        """
        :param: region: the query region
        :return: iterator that contains all required entities
        """
        return self._entities.select_by_region(region)

    def entities_of_type_in_region(self, q_type, region) -> iter:
        """
        :param: region: the query region
        :param: q_type: the query type
        :return: iterator that contains all required entities
        """
        return self._entities.select_type_in_region(q_type, region)

    """
        Define listener as a property which returns a iterator. Adding or Deleting listeners could only use functions
        add_listener() and remove_listener(). By adding (or removing) a listener we call its on_added()
         (or on_removed()) function.
    """
    @property
    def listeners(self):
        return self._listeners.__iter__()

    def add_listener(self, new_listener):
        new_listener.scene = self
        self._listeners.append(new_listener)
        new_listener.on_added()

    def remove_listener(self, listener):
        self._listeners.remove(listener)
        listener.on_removed(self)

    def begin(self):
        """
        Call all listener's on_begin
        """
        for lis in self.listeners:
            lis.on_begin()

    def step_next(self):
        # call model to step next
        self.model.step_next(self)
        # time_step increment
        self.time_step += 1

        # call listeners
        for lis in self.listeners:
            lis.on_stepped()

    def run(self):
        """ When called run(), scene thread will first call begin() then automatically step_next()
         
        """
        self.begin()  # pack up
        while True:
             self.step_next()  # step next

    def stop(self):
        self._is_stopped = True  # inherit from class Thread


class SceneListener(ABC):

    def __init__(self):
        self.scene = None

    @abstractmethod
    def on_added(self):
        """ Define listener's behaviour after being added

        """
        pass

    @abstractmethod
    def on_begin(self):
        """ Define listener's behavior before the scene begin to start

        """
        pass

    @abstractmethod
    def on_stepped(self):
        """ Define listener's behavior after each step

        """
        pass

    @abstractmethod
    def on_removed(self):
        """ Define listener's behavior after being removed

        """
        pass
