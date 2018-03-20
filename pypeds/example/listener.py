from pypeds.scene import SceneListener
from pypeds.entity import Agent
import math

class PedestrianEscapeListener(SceneListener):
    def on_added(self):
        pass

    def on_begin(self):
        pass

    def on_stepped(self):
        for agent in self.scene.entities_of_type(Agent):
            if agent.escaped:
                self.scene.remove_entity(agent)

    def on_removed(self):
        pass
