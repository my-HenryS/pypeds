from pypeds.entity import *
from pypeds.pool import *
from abc import ABC, abstractmethod

__all__ = ['Scene', 'SceneListener']


class Scene(object):

    def __init__(self, entities=None, model=None):
        """ Define operations to the variable 'entities'.
        We here define a entities pool and restrict modifying it only with functions
        add_entity() and remove_entity(). We use EntityPool.get() to get a proportion of entities of a specific type.

        """
        self.entities = EntityPool(entities)
        self.model = model
        self.time_step = 0
        self.__listeners = []
        self.drawer = None

    """
    Add and remove entity
    
    """
    def add_entity(self, new_entity):
        self.entities.add(new_entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    @property
    def agents(self) -> iter:
        """
        :return: iterator that contains all agents
        """
        return self.entities.select(Agent)

    """
        Define listener as a property which returns a iterator. Adding or Deleting listeners could only use functions
        add_listener() and remove_listener(). By adding (or removing) a listener we call its on_added()
         (or on_removed()) function.
    """
    @property
    def listeners(self):
        return self.__listeners.__iter__()

    def add_listener(self, new_listener):
        self.__listeners.append(new_listener)
        new_listener.on_added(self)

    def remove_listener(self, listener):
        self.__listeners.remove(listener)
        listener.on_removed(self)

    # TODO Formally define step_next here using block comments
    def step_next(self):
        # call model to step next
        # self.model.step_next(self.entities) TODO remove comment

        # time_step increment
        self.time_step += 1

        # call listeners
        for lis in self.listeners:
            lis.on_stepped()


class SceneListener(ABC):

    def __init__(self, scene=None):
        self.scene = scene

    @abstractmethod
    def on_added(self, scene):
        """ Define lister's behavior after being added

        """
        pass

    @abstractmethod
    def on_stepped(self):
        """ Define lister's behavior after each step

        """
        pass

    @abstractmethod
    def on_removed(self):
        """ Define lister's behavior after being removed

        """
        pass
