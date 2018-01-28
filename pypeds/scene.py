from pypeds.entity import *
from pypeds.pool import *

__all__ = ['Scene']


class Scene(object):
    def __init__(self, entities=None, model=None):
        self.__entities = EntityPool(entities)
        self.model = model

    """Define operation to the variable 'entities'.

    We here define entities pool as private variable and restrict modifying it only with functions
    add_entity() and remove_entity(). We use EntityPool.get() to get a proportion of entities of a specific type.

    """

    @property
    def entities(self) -> iter:
        """
        :return: iterator that contains all entities
        """
        return self.__entities.select(Entity)

    # add and remove entity
    def add_entity(self, new_entity):
        self.__entities.add(new_entity)

    def remove_entity(self, entity):
        self.__entities.remove(entity)

    @property
    def agents(self) -> iter:
        """
        :return: iterator that contains all agents
        """
        return self.__entities.select(Agent)

    def start(self):
        for agent in self.agents:
            pass
