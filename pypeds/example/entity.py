from pypeds.entity import *
from pypeds.shape2d import *

class Pedestrian(Agent):
    def __init__(self, shape):
        super(Pedestrian, self).__init__(shape)
        self.mass = 80

    def to_dict(self):
        return {"Pedestrian": {"shape": self.shape.to_dict(), "velocity": self.velocity, "mass": self.mass}}

    def from_dict(self, s_dict):
        """
        read from s_dict to generate a pedestrian
        :param s_dict:
        :return:
        """
        shape = s_dict["Pedestrian"]["shape"]
        velocity = s_dict["Pedestrian"]["velocity"]
        mass = s_dict["Pedestrian"]["mass"]
        return Pedestrian(shape)


class Wall(Movable):
    def __init__(self,shape):
        super(Wall, self).__init__(shape)

    def affected(self, affection):
        pass

    def to_dict(self):
        return {"Wall": {"shape": self.shape.to_dict()}}

    def from_dict(self, s_dict):
        """
        read from s_dict to generate a wall
        :param s_dict:
        :return:
        """
        shape = s_dict["Wall"]["shape"]
        return Wall(shape)


class SafetyRegion(Goal):
    pass


class RotatePedestrian(RotateAgent):
    def __init__(self, shape):
        super(RotatePedestrian, self).__init__(shape)
        self.mass = 80
        self.inertia = 4

    TODO

    def to_dict(self):
        return {"RotatePedestrian": {"shape": self.shape.to_dict(), "velocity": self.velocity, "mass": self.mass}}

    def from_dict(self, s_dict):
        """
        read from s_dict to generate a pedestrian
        :param s_dict:
        :return:
        """
        shape = s_dict["pedestrian"]["shape"]
        velocity = s_dict["pedestrian"]["velocity"]
        mass = s_dict["pedestrian"]["mass"]
        return Pedestrian(shape)
