from pypeds.entity import Agent
from pypeds.scene import SceneListener
import math
import time


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


class Average_velocity(SceneListener):
    def __init__(self, window):
        super(Average_velocity, self).__init__()
        self.window = window

    def on_added(self):
        pass

    def on_begin(self):
        pass

    def on_stepped(self):
        if self.scene.time_step % 50 == 0:
            sum_average = 0
            number = 0
            for agent in self.scene.entities_of_type(Agent):
                sum_average = sum_average + math.sqrt(agent.velocity.x ** 2 + agent.velocity.y ** 2)
                number += 1
            if number != 0:
                self.window.lineEdit.setText(str(sum_average / number))

    def on_removed(self):
        pass


class timer(SceneListener):
    def __init__(self, window):
        super(timer, self).__init__()
        self.window = window

    def on_added(self):
        pass

    def on_begin(self):
        pass

    def on_stepped(self):
        if self.scene.time_step % 100 == 0:
            self.window.lineEdit_2.setText(str(self.scene.time_step / 100))

    def on_removed(self):
        pass
