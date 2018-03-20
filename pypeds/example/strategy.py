from pypeds.entity import Goal
from pypeds.shape2d import Point2D
from pypeds.strategy import Strategy, Path


class NearestGoalStrategy(Strategy):

    def on_begin(self):
        """
        Set agents' paths on scene begin
        """
        for agent in self.agents:
            dsr_dist, dsr_goal = min((goal.distance(agent), goal.position) for goal in self.scene.entities_of_type(Goal))
            agent.path = StraightPath(dsr_goal)

    def on_stepped(self):
        pass


class StraightPath(Path):
    def __init__(self, goal):
        self.goal = goal

    def next_step(self, pos):
        return (self.goal - pos).unit()
