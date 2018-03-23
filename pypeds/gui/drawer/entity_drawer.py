from abc import ABC, abstractmethod

# TODO write docs, implement AgentDrawer, etc.


class EntityDrawer(ABC):
    def __init__(self, device, register):
        self.device = device
        self.shape_register = register

    def draw(self, entity):
        if entity.shape.drawer is not None:
            entity.shape.drawer.draw(entity.shape)
        else:
            self.shape_register.add_drawer_support(entity.shape)
            entity.shape.drawer.draw(entity.shape)
