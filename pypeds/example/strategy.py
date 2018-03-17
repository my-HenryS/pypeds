from pypeds.shape2d import Point2D
from pypeds.strategy import Strategy, Path
from pypeds.gui.panel import *


class NearestGoalStrategy(Strategy):

    def on_begin(self):
        """
        Set agents' paths on scene begin
        """
        for agent in self.agents:
            agent.path = StraightPath(Point2D(int(
                [x for x in self.scene._listeners if isinstance(x, Panel)][0].window.settingwindow.lineEdit_33.text()),
                int([x for x in self.scene._listeners if isinstance(x, Panel)][
                        0].window.settingwindow.lineEdit_33.text())))

    def on_stepped(self):
        pass


class StraightPath(Path):
    def __init__(self, goal):
        self.goal = goal

    def next_step(self, pos):
        return (self.goal - pos).unit()
