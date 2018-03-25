from pypeds.entity import Goal
from pypeds.shape2d import Point2D, Circle2D
from pypeds.strategy import Strategy, Path, StaticStrategy
from pypeds.utils import shortest_path

class NearestGoalStrategy(StaticStrategy):

    def on_begin(self):
        """
        Set agents' paths on scene begin
        """
        for agent in list(set(self.agents).union(set(self.rotateagent))):
            dsr_dist, dsr_goal = min((goal.distance(agent), goal.position) for goal in self.scene.entities_of_type(Goal))
            agent.path=StraightPath(dsr_goal)
            # agent.path = GridPath.create_path(self.scene, Circle2D(Point2D(0,0),1),dsr_goal)    # TODO implement path factory

    def on_stepped(self):
        pass


class StraightPath(Path):
    def __init__(self, goal):
        self.goal = goal

    def next_step(self, pos):
        return (self.goal - pos).unit()


class GridPath(Path):
    def __init__(self, field, dist_field, div, offset):
        self.field = field
        self.offset = offset
        self.div = div
        self.dist_field = dist_field

    def next_step(self, pos):
        translated = (pos - self.offset) / self.div
        x, y = translated.x, translated.y
        direction = (self.field[int(x)][int(y)] - Point2D(int(x),int(y))).unit()
        return direction

    @staticmethod
    def create_path(scene, shape, dest, div=0.4):
        grid, offset = scene.to_grid(shape, div)
        translated_dest = (dest - offset) / div
        field, dist_field = shortest_path(grid, translated_dest)
        return GridPath(field, dist_field, div, offset)