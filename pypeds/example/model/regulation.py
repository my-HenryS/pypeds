from pypeds.example.entity import *
from pypeds.entity import *
from pypeds.model.affection import Affection
from pypeds.model.regulation import SingleTargetRegulation, Regulation, SelfDrivenRegulation
import math


from pypeds.shape2d import Vector2D, Ellipse2D


class PsychologicalForceRegulation(SingleTargetRegulation):

    def __init__(self, model):
        super().__init__(model)
        self._source_class = Movable
        self._target_class = Agent

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
        if hasattr(target, "is_rotate") and target.is_rotate:
            m_dist, m_dirt = source.shape.distance(target.shape.center)
            l_dist, l_dirt = source.shape.distance(target.shape.c_left)
            r_dist, r_dirt = source.shape.distance(target.shape.c_right)
            m_dist -= target.shape.b
            l_dist -= (target.shape.a - target.shape.b) / 2
            r_dist -= (target.shape.a - target.shape.b) / 2
            if dist == m_dist:
                return
            elif dist == l_dist:
                length_dist, length_dirt = DistanceCalculator.distance(target.shape.center,target.shape.c_left)
            else:
                length_dist, length_dirt = DistanceCalculator.distance(target.shape.center,target.shape.c_right)
            length = length_dirt * length_dist
            torque = length.x * force.y - force.x * length.y
            affection = Affection("Torque", torque)
            target.affected(affection)


class BodyForceRegulation(SingleTargetRegulation):

    def __init__(self, model):
        super().__init__(model)

        self._source_class =Movable
        self._target_class = Agent

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
        target.affected(affection)
        if hasattr(target, "is_rotate") and target.is_rotate:
            m_dist, m_dirt = source.shape.distance(target.shape.center)
            l_dist, l_dirt = source.shape.distance(target.shape.c_left)
            r_dist, r_dirt = source.shape.distance(target.shape.c_right)
            m_dist -= target.shape.b
            l_dist -= (target.shape.a - target.shape.b) / 2
            r_dist -= (target.shape.a - target.shape.b) / 2
            if dist == m_dist:
                return
            elif dist == l_dist:
                length_dist, length_dirt = DistanceCalculator.distance(target.shape.center, target.shape.c_left)  #fixme force point calculation
            else:
                length_dist, length_dirt = DistanceCalculator.distance(target.shape.center, target.shape.c_right)
            length = length_dirt * length_dist
            torque = length.x * force.y - force.x * length.y
            affection = Affection("Torque", torque)
            target.affected(affection)


class SelfDrivenForceRegulation(SelfDrivenRegulation):
    def __init__(self, model, expected_velocity, react_time):
        super().__init__(model)

        self._source_class = Agent
        self._target_class = Agent
        self.exp_v = expected_velocity
        self.react_t = react_time

    def exert(self, entity):
        dirt = entity.next_step()
        force = (dirt * self.exp_v - entity.velocity) * (entity.mass / self.react_t)
        affection = Affection("Force", force)
        entity.affected(affection)


class SelfDrivenTorqueRegulation(SelfDrivenRegulation):
    def __init__(self, model):
        super().__init__(model)

        self._source_class = RotatePedestrian
        self._target_class = RotatePedestrian

    def exert(self, entity):
        dirt = entity.next_step()
        face = Vector2D( math.sin(entity.angle),- math.cos(entity.angle))
        result=dirt.x * face.x + dirt.y * face.y
        if result>1:
            result=1
        rotate_angle = math.acos(result)
        if result < 0:
            rotate_angle *= -1
        torque = 40 * abs(rotate_angle)
        affection = Affection("Torque", torque)
        entity.affected(affection)


class SelfDampingTorqueRegulation(SelfDrivenRegulation):
    def __init__(self, model, react_time):
        super().__init__(model)

        self._source_class = RotatePedestrian
        self._target_class = RotatePedestrian
        self.react_t = react_time

    def exert(self, entity):
        torque = (-5 * entity.palstance) * (entity.inertia / self.react_t)
        affection = Affection("Torque", torque)
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
