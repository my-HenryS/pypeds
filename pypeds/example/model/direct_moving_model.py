from pypeds.entity import Agent
from pypeds.model.affection import Affection
from pypeds.model.model import *
from pypeds.shape2d import Vector2D


class DirectMovingModel(Model):

    def __init__(self, time_per_step):
        super().__init__(time_per_step)

    def zero_angular_velocity(self):
        return 0

    def zero_velocity(self):
        return Vector2D(0, 0)

    def step_next(self, scene):
        for agent in scene.entities_of_type(Agent):
            agent.affected(affection=Affection("Force", Vector2D(7,7)))

        import time
        time.sleep(0.001)