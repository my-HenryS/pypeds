from pypeds.example.entity import *
from pypeds.entity import Blockable
from pypeds.model.regulation import Regulation


class PsychologicalForceRegulation(Regulation):
    def __init__(self, model):
        super().__init__(model)

        self._is_multiple = False
        self._source_class = Blockable
        self._target_class = Pedestrian

    def exert(self, source, target):


        pass


class BodyForceRegulation(Regulation):
    def __init__(self, model):
        super().__init__(model)

        self._is_multiple = False
        self._source_class = Blockable
        self._target_class = Pedestrian

    def exert(self, source, target):


        pass


class SelfDrivenForceRegulation(Regulation):
    def __init__(self, model):
        super().__init__(model)

        self._is_multiple = False
        self._source_class = Pedestrian
        self._target_class = Pedestrian

    def exert(self, source, target):


        pass