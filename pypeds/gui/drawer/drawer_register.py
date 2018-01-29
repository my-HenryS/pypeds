from abc import ABC, abstractmethod
from pypeds.shape import *
from pypeds.scene import *
from .shape_drawer import *
from .scene_drawer import *

# TODO write docs

class DrawerRegister(ABC):
    def __init__(self, device, mode="default"):
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

    def default_register(self):
        self.register(Circle2D, Circle2DDrawer(self.device))

    def add_drawer_support(self, shape) -> bool:
        drawer = self.drawer_map[type(shape)]
        if drawer is not None:
            shape.drawer = drawer
            return True

        return False


class SceneDrawerRegister(DrawerRegister):

    def __init__(self, device, mode="default"):
        super().__init__(device, mode)
        self.shape_drawer_register = None
        if mode == "default":
            self.shape_drawer_register = ShapeDrawerRegister(device, mode)

    def default_register(self):
        self.register(Scene, SceneDrawer(self.device))

    def add_drawer_support(self, scene) -> bool:
        drawer = self.drawer_map[type(scene)]
        if drawer is not None:
            scene.drawer = drawer
            for entity in scene.entities:   # TODO modify this line after implemented entity drawer and entity installer
                self.shape_drawer_register.add_drawer_support(entity.shape)
            return True

        return False
