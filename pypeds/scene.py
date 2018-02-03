from pypeds.pool import EntityPool
from pypeds.entity import Entity
from abc import ABC, abstractmethod
from threading import Thread


class Scene(Thread):

    def __init__(self, model=None):
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

    @property
    def entities(self):
        return self._entities.select_all(Entity)
    """
    Add and remove entity
    
    """
    def add_entity(self, new_entity):
        self._entities.add(new_entity)
        new_entity.model = self.model

    def remove_entity(self, entity):
        self._entities.remove(entity)

    def select_all(self, q_type) -> iter:
        """
        :param: q_type: the query type
        :return: iterator that contains all required entities
        """
        return self._entities.select_all(q_type)

    """
        Define listener as a property which returns a iterator. Adding or Deleting listeners could only use functions
        add_listener() and remove_listener(). By adding (or removing) a listener we call its on_added()
         (or on_removed()) function.
    """
    @property
    def listeners(self):
        return self._listeners.__iter__()

    def add_listener(self, new_listener):
        self._listeners.append(new_listener)
        new_listener.on_added(self)

    def remove_listener(self, listener):
        self._listeners.remove(listener)
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

    def start(self):
        """ When called run(), scene thread will automatically step_next()
         
        """
        while True:
            self.step_next()


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
