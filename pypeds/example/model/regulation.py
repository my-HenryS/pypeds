from pypeds.example.entity import *
from pypeds.entity import Blockable
from pypeds.model.regulation import SingleTargetRegulation, Regulation


class PsychologicalForceRegulation(SingleTargetRegulation):
    def __init__(self, model):
        super().__init__(model)

        self._is_multiple = False
        self._source_class = Blockable
        self._target_class = Pedestrian

    def exert_single(self, source, target):


        pass


class BodyForceRegulation(SingleTargetRegulation):
    def __init__(self, model):
        super().__init__(model)

        self._is_multiple = False
        self._source_class = Blockable
        self._target_class = Pedestrian

    def exert_single(self, source, target):


        pass


class SelfDrivenForceRegulation(SingleTargetRegulation):
    def __init__(self, model):
        super().__init__(model)

        self._is_multiple = False
        self._source_class = Pedestrian
        self._target_class = Pedestrian

    def exert_single(self, source, target):


        pass