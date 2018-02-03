from abc import ABC, abstractmethod

# TODO write docs, implement AgentDrawer, etc.


class EntityDrawer(ABC):
    def __init__(self, device):
        self.device = device

    def draw(self, entity):
        entity.shape.drawer.draw(entity.shape)
