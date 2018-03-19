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


class Average_velocity(SceneListener):
    """
    listener to show the average velocity in the main window
    """

    def on_added(self):
        pass

    def on_begin(self):
        pass

    def on_stepped(self):
        from pypeds.gui.panel import Panel
        if self.scene.time_step % 50 == 0:
            sum_average = 0
            number = 0
            for agent in self.scene.entities_of_type(Agent):
                sum_average = sum_average + math.sqrt(agent.velocity.x ** 2 + agent.velocity.y ** 2)
                number += 1
            if number != 0:
                [x for x in self.scene._listeners if isinstance(x,Panel)][0].window.lineEdit.setText(str(sum_average/number))

    def on_removed(self):
        pass


class timer(SceneListener):
    """
    listener to show the running time in the main window
    """

    def on_added(self):
        pass

    def on_begin(self):
        pass

    def on_stepped(self):
        from pypeds.gui.panel import Panel
        if self.scene.time_step % 100 == 0:
            [x for x in self.scene._listeners if isinstance(x,Panel)][0].window.lineEdit_2.setText(str(self.scene.time_step/100))

    def on_removed(self):
        pass
