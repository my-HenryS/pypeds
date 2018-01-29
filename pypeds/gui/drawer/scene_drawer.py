# TODO write docs

class SceneDrawer(object):
    def __init__(self, device):
        self.device = device
        self.background_color = "black"

    def draw(self, scene):
        for entity in scene.entities:  # TODO modify this line after implemented entity drawer and entity installer
            entity.shape.drawer.draw(entity.shape)

