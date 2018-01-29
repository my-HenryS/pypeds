from abc import ABC, abstractmethod


class Model(ABC):

    def __init__(self, time_per_step, regulations = None):
        self.time_per_step = time_per_step
        self.regulations = regulations

    @abstractmethod
    def step_next(self, entities):
        """ Define how will the model controls each entity's movement (or other changes in their attributes)

        :param entities:
        :return:
        """
        pass