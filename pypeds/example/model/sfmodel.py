from pypeds.model.model import *
from pypeds.example.model.regulation import *
from pypeds.shape2d import Vector2D


class SFModel(Model):

    def __init__(self, time_per_step):
        super().__init__(time_per_step)
        self.regulations = []
        self.regulations.append(PsychologicalForceRegulation(self))
        self.regulations.append(BodyForceRegulation(self))
        self.regulations.append(SelfDrivenForceRegulation(self, 3, 0.5))
        self.regulations.append(SelfDrivenTorqueRegulation(self))
        self.regulations.append(SelfDampingTorqueRegulation(self, 0.5))
        self.regulations.append(EscapeRegulation(self))

    def zero_angular_velocity(self):
        return 0

    def zero_velocity(self):
        return Vector2D(0, 0)

