from pypeds.shape2d import Point2D
from pypeds.strategy import Strategy, Path


class NearestGoalStrategy(Strategy):
    def on_begin(self):
        """
        Set agents' paths on scene begin
        """
        for agent in self.agents:
            agent.path = StraightPath(Point2D(200, 200))   # TODO remove hard code

    def on_stepped(self):
        pass


class StraightPath(Path):
    def __init__(self, goal):
        self.goal = goal

    def next_step(self, pos):
        return (self.goal - pos).unit()