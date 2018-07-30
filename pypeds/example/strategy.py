from pypeds.entity import Goal
from pypeds.shape2d import Point2D, Circle2D
from pypeds.strategy import Strategy, Path, StaticStrategy
from pypeds.utils import shortest_path

class NearestGoalStrategy(StaticStrategy):

    def __init__(self):
        self.dict = {}

    def on_begin(self):
        """
        Set agents' paths on scene begin
        """
        goals = self.scene.entities_of_type(Goal)
        for goal in goals:
            self.dict[goal.position] = GridPath.create_path(self.scene, Circle2D(Point2D(0, 0), 0.45/2), goal.position)

        for agent in self.agents:
            dsr_dist, dsr_goal = min(
                (goal.distance(agent), goal.position) for goal in self.scene.entities_of_type(Goal))
            agent.path = self.dict[dsr_goal]  # TODO implement path factory

        pass

    def on_stepped(self):
        pass

class StraightPath(Path):
    def __init__(self, goal):
        self.goal = goal

    def next_step(self, pos):
        return (self.goal - pos).unit()

import random
class GridPath(Path):
    def __init__(self, field, dist_field, div, offset):
        self.field = field
        self.offset = offset
        self.div = div
        self.dist_field = dist_field

    def next_step(self, pos):
        translated = (pos - self.offset) / self.div
        x, y = int(translated.x), int(translated.y)
        next = self.field[int(x)][int(y)]
        if isinstance(next,int):
            break_flag = False
            h = 0
            while not break_flag and h >= 0:
                for i in range(x-1-h,x+2+h):
                    for j in range(y-1-h,y+2+h):
                        next = self.field[int(i)][int(j)]
                        if not isinstance(next,int):
                            break_flag = True
                            break
                    if break_flag:
                        break
        direction = (next - Point2D(x,y)).unit()
        return direction

    @staticmethod
    def create_path(scene, shape, dest, div=0.2):
        grid, offset = scene.to_grid(shape, div)
        translated_dest = (dest - offset) / div
        field, dist_field = shortest_path(grid, translated_dest)
        return GridPath(field, dist_field, div, offset)