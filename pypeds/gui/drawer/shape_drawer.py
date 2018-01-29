from abc import ABC, abstractmethod

# TODO write docs


class ShapeDrawer(ABC):
    def __init__(self, device):
        self.device = device
        self.default_color = "black"

    @abstractmethod
    def render(self, shape, color):
        pass

    def draw(self, shape):
        self.render(shape, self.default_color)


class Circle2DDrawer(ShapeDrawer):
    def __init__(self, device):
        super().__init__(device)

    def render(self, shape, color):
        x, y = shape.center
        r = shape.radius
        self.device.create_oval(x, y, (x+2*r), (y+2*r), fill=color)

