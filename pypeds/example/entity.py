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
        read from s_dict to generate a Pedestrian
        :param s_dict:
        :return:
        """
        shape = s_dict["Pedestrian"]["shape"]
        velocity = s_dict["Pedestrian"]["velocity"]
        mass = s_dict["Pedestrian"]["mass"]
        ped = Pedestrian(shape)
        ped.velocity = velocity
        ped.mass = mass
        return ped


class Wall(Movable):
    def __init__(self,shape):
        super(Wall, self).__init__(shape)

    def affected(self, affection):
        pass

    def to_dict(self):
        return {"Wall": {"shape": self.shape.to_dict()}}

    def from_dict(self, s_dict):
        """
        read from s_dict to generate a Wall
        :param s_dict:
        :return:
        """
        shape = s_dict["Wall"]["shape"]
        return Wall(shape)


class SafetyRegion(Goal):
    pass

    def to_dict(self):
        return {"SafetyRegion": {"shape": self.shape.to_dict()}}

    def from_dict(self, s_dict):
        """
        read from s_dict to generate a SafetyRegion
        :param s_dict:
        :return:
        """
        shape = s_dict["SafetyRegion"]["shape"]
        return SafetyRegion(shape)


class RotatePedestrian(RotateAgent):
    def __init__(self, shape):
        super(RotatePedestrian, self).__init__(shape)
        self.mass = 80
        self.inertia = 4

    def to_dict(self):
        return {"RotatePedestrian": {"shape": self.shape.to_dict(), "velocity": self.velocity, "palstance": self.palstance, "inertia": self.inertia, "mass": self.mass}}

    def from_dict(self, s_dict):
        """
        read from s_dict to generate a RotatePedestrian
        :param s_dict:
        :return:
        """
        shape = s_dict["RotatePedestrian"]["shape"]
        velocity = s_dict["RotatePedestrian"]["velocity"]
        palstance = s_dict["RotatePedestrian"]["palstance"]
        inertia = s_dict["RotatePedestrian"]["inertia"]
        mass = s_dict["RotatePedestrian"]["mass"]
        ped = RotatePedestrian(shape)
        ped.palstance = palstance
        ped.velocity = velocity
        ped.inertia = inertia
        ped.mass = mass
        return ped
