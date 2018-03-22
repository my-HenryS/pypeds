from abc import ABC, abstractmethod
from pypeds.shape2d import *
from pypeds.scene import *
from pypeds.entity import *
from pypeds.gui.drawer.shape_drawer import *
from pypeds.gui.drawer.scene_drawer import *
from pypeds.gui.drawer.entity_drawer import *


# TODO write docs


class DrawerRegister(ABC):
    def __init__(self, device=None, mode="default"):
        self.device = device

        # drawer_map : drawer -> drawable_type
        self.drawer_map = {}
        if mode == "default":
            self.default_register()

    def register(self, drawable_type, drawer):
        self.drawer_map[drawable_type] = drawer

    @abstractmethod
    def default_register(self):
        pass

    @abstractmethod
    def add_drawer_support(self, drawable) -> bool:
        pass


class ShapeDrawerRegister(DrawerRegister):
    # there are no inheritance between shapes
    def default_register(self):
        self.register(Circle2D, Circle2DDrawer(self.device))  # FIXME remove hard code
        self.register(Box2D, Box2DDrawer(self.device))
        self.register(Ellipse2D, Ellipse2DDrawer(self.device))

    def add_drawer_support(self, shape) -> bool:
        """ Find the exact shape drawer

        :param shape: shape
        :return: success or not
        """
        drawer = self.drawer_map[type(shape)]
        if drawer is not None:
            shape.drawer = drawer
            return True

        return False


class EntityDrawerRegister(DrawerRegister):
    # there are inheritance between entities
    def __init__(self, device, mode="default"):
        self.shape_drawer_register = ShapeDrawerRegister(device, mode)
        super().__init__(device, mode)

    def default_register(self):
        self.register(Entity, EntityDrawer(self.device, self.shape_drawer_register))  # FIXME remove hard code

    def add_drawer_support(self, entity) -> bool:
        """ Find the first-matched entity drawer by matching either the entity class itself or any of its super classes
           and register drawers for it shapes

        :param entity: entity
        :return: success or not
        """
        drawer = None
        for d_type in self.drawer_map:
            if issubclass(type(entity), d_type):
                drawer = self.drawer_map[d_type]
        if drawer is not None:
            entity.drawer = drawer
            self.shape_drawer_register.add_drawer_support(entity.shape)
            return True

        return False


class SceneDrawerRegister(DrawerRegister):

    def __init__(self, device, mode="default"):
        self.entity_drawer_register = EntityDrawerRegister(device, mode)
        super().__init__(device, mode)

    def default_register(self):
        self.register(Scene, SceneDrawer(self.device, self.entity_drawer_register))  # FIXME remove hard code

    def add_drawer_support(self, scene) -> bool:
        """ Find the scene drawer and register all drawers for its entities

        :param scene: scene
        :return: success or not
        """
        drawer = self.drawer_map[type(scene)]
        if drawer is not None:
            scene.drawer = drawer
            for entity in scene.entities:
                self.entity_drawer_register.add_drawer_support(entity)
            return True

        return False
