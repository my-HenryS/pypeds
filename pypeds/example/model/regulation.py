from pypeds.example.entity import *
from pypeds.entity import Blockable
from pypeds.model.affection import Affection
from pypeds.model.regulation import SingleTargetRegulation, Regulation, SelfDrivenRegulation
import math


# TODO Resolve view problem

class PsychologicalForceRegulation(SingleTargetRegulation):

    def __init__(self, model):
        super().__init__(model)
        self._source_class = Blockable
        self._target_class = Pedestrian

    @property
    def A(self):
        return 2000

    @property
    def B(self):
        return 0.08

    @property
    def view(self):     # regulation exists only when source and target has a dist >= view
        return 3

    def exert_single(self, source, target):
        if source is target:
            return
        dist, dirt = source.distance(target)
        if dist < self.view:
            return
        force = dirt * (self.A * math.exp(-dist) / self.B)
        affection = Affection("Force", force)
        target.affected(affection)


class BodyForceRegulation(SingleTargetRegulation):

    def __init__(self, model):
        super().__init__(model)

        self._source_class = Blockable
        self._target_class = Pedestrian

    @property
    def k1(self):
        return 1.2 * 100000

    @property
    def k2(self):
        return 2.4 * 100000

    def exert_single(self, source, target):
        if source is target:
            return
        dist, dirt = source.distance(target)
        if dist > 0:     # regulation exists only when two entities intersects
            return
        # calculate medium vectors
        v_diff_unit = (source.velocity - target.velocity).unit()  # unit vector of velocity difference
        vert = dirt.get_rotation(math.pi / 2)
        # calculate body_force and sliding_force
        body_force = dirt * (self.k1 * abs(dist))
        sliding_force = vert * (self.k2 * abs(dist)) * (vert * v_diff_unit)
        force = body_force + sliding_force
        affection = Affection("Force", force)
        target.affected(affection)     # TODO do not modify target directly (controversial)


class SelfDrivenForceRegulation(SelfDrivenRegulation):
    def __init__(self, model, expected_velocity, react_time):
        super().__init__(model)

        self._source_class = Pedestrian
        self._target_class = Pedestrian
        self.exp_v = expected_velocity
        self.react_t = react_time

    def exert(self, entity):
        dirt = entity.next_step()
        force = (dirt * self.exp_v - entity.velocity) * (entity.mass / self.react_t)
        affection = Affection("Force", force)
        entity.affected(affection)


class EscapeRegulation(SingleTargetRegulation):    # TODO separate into two regulations
    def __init__(self, model):
        super().__init__(model)

        self._source_class = SafetyRegion
        self._target_class = Escapable

    def exert_single(self, source, target):
        dist, dirt = source.distance(target)
        if dist > 0:
            return
        target.affected(Affection("Escape", True))
        source.affected(Affection("Record", target))
