# TODO write docs


class SceneDrawer(object):
    def __init__(self, device, register):
        self.device = device
        self.background_color = "black"
        self.entity_register = register

    def draw(self, scene):
        for entity in scene.entities:
            if entity.drawer is not None:
                entity.drawer.draw(entity)
            else:
                self.entity_register.add_drawer_support(entity)
                entity.drawer.draw(entity)

