from pypeds.example.entity import *
from pypeds.entity import Blockable
from pypeds.model.affection import Affection
from pypeds.model.regulation import SingleTargetRegulation, Regulation
import math


class PsychologicalForceRegulation(SingleTargetRegulation):

    def __init__(self, model):
        super().__init__(model)

        self._is_multiple = False
        self._source_class = Blockable
        self._target_class = Pedestrian

    @property
    def A(self):
        return 2000

    @property
    def B(self):
        return 0.08

    def exert_single(self, source, target):
        dist, dirt = source.distance(target)
        force = dirt * (self.A * math.exp(-dist) / self.B)
        affection = Affection("Force", force)
        target.affected(affection)


class BodyForceRegulation(SingleTargetRegulation):

    def __init__(self, model):
        super().__init__(model)

        self._is_multiple = False
        self._source_class = Blockable
        self._target_class = Pedestrian

    @property
    def k1(self):
        return 1.2 * 100000

    @property
    def k2(self):
        return 2.4 * 100000

    def exert_single(self, source, target):
        dist, dirt = source.distance(target)
        if dist > 0:
            return
        # calculate medium vectors
        v_diff_unit = (source.velocity - target.velocity).unit()  # unit vector of velocity difference
        vert = dirt.get_rotation(math.pi / 2)
        # calculate body_force and sliding_force
        body_force = dirt * (self.k1 * abs(dist))
        sliding_force = vert * (self.k2 * abs(dist) * vert * v_diff_unit)
        force = body_force + sliding_force
        affection = Affection("Force", force)
        target.affected(affection)     # TODO do not modify target directly


class SelfDrivenForceRegulation(SingleTargetRegulation):
    def __init__(self, model):
        super().__init__(model)

        self._is_multiple = False
        self._source_class = Pedestrian
        self._target_class = Pedestrian

    def exert_single(self, source, target):

        pass