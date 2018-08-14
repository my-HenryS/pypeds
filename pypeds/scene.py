from pypeds.example.entity import Wall
from pypeds.pool import EntityPool
from pypeds.entity import Entity
from abc import ABC, abstractmethod
from threading import Thread
from pypeds.shape2d import *
import time
from pypeds.example.model.csvmodel import *
from pypeds.generator import *

class Scene(Thread):

    def __init__(self, model=None, strategy=None):
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
        self._is_paused = False
        self.bound = None
        self.generator = Generator(self)

    @property
    def entities(self):
        return self._entities.select_by_type(Entity)

    """
    Add and remove entity
    
    """

    def add_model(self, model):
        self.model = model
        if isinstance(model, CSVModel):
            model.on_add()

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
        listener.on_removed()

    def pack(self, margin=10):
        y_max = max(entity.shape.bound.y_max for entity in self.entities)
        y_min = min(entity.shape.bound.y_min for entity in self.entities)
        x_max = max(entity.shape.bound.x_max for entity in self.entities)
        x_min = min(entity.shape.bound.x_min for entity in self.entities)
        self.bound = Box2D(Point2D((x_max + x_min) / 2, (y_max + y_min) / 2), x_max - x_min + margin * 2,
                           y_max - y_min + margin * 2)

    def begin(self):
        """
        Pack up scene. Call all listener's on_begin
        """
        self.pack()
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
        while not self._is_stopped:
            self.step_next()  # step next
            while self._is_paused:
                time.sleep(100)

    def stop(self):
        self._is_stopped = True  # inherit from class Thread

    def pause(self):
        self._is_paused = True

    def resume(self):
        self._is_paused = False

    def to_grid(self, shape, div=0.4, default_value=0, block_value=1, run_off_rate=5):
        """ Meshing the scene into grid, setting each cell with values that represents its accessibility by agents.

        We classify entities in scene into blockable entities and other entities. When the 'shape' being placed in a cell
         of the grid intersects with any blockable entity, we set the value of cell to 'block_value'.
         Otherwise (aka 'shape' does not hit any blockable entities), we set the value to 'default_value'.
        :param shape: the shape of agent
        :param div: the division of cell (square)
        :param default_value: value of accessible cell
        :param block_value:  value of inaccessible cell
        :return: grid: the grid of scene
        """
        import copy
        template_shape = copy.deepcopy(shape)
        if self.bound is None:
            raise NotImplementedError

        length = int(self.bound.length / div) + 1
        width = int(self.bound.width / div) + 1
        x_min = self.bound.x_min
        y_min = self.bound.y_min

        grid = [[0 for i in range(width)] for j in range(length)]

        for j in range(width):
            for i in range(length):
                pos = Point2D(x_min + div * i, y_min + div * j)
                template_shape.center = pos
                grid[i][j] = default_value
                for entity in self.entities_of_type(Wall):
                    if entity.shape.intersects(template_shape, run_off_rate * div):
                        grid[i][j] = block_value
                        break

        return grid, Point2D(x_min, y_min)


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
