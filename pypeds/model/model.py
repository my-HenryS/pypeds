from abc import ABC, abstractmethod
from pypeds.example.model.csvregulation import *
from pypeds.model.regulation import SelfDrivenRegulation, Regulation


class Model(ABC):

    def __init__(self, time_per_step, regulations=None):
        self.time_per_step = time_per_step
        self.regulations = regulations or []


    def step_next(self, scene):
        """ Define how will the model controls each entity's movement (or other changes in their attributes)

        :param scene:
        :return:
        """
        # time.sleep(self.time_per_step)    # FIXME  implement frame lock
        for regulation in self.regulations:
            if isinstance(regulation, SelfDrivenRegulation):
                s_class = regulation.source_class
                sources = scene.entities_of_type(s_class)
                for source in sources:
                    regulation.exert(source)

            elif isinstance(regulation, Regulation):
                # get interact classes
                s_class = regulation.source_class
                t_class = regulation.target_class

                # select interact entities
                sources = scene.entities_of_type(s_class)
                # exert
                for source in sources:
                    # select affected entities in view
                    targets_in_view = scene.entities_of_type(t_class)
                    # let source exert affection on targets in view
                    regulation.exert(source, targets_in_view)

            # have changed here
            elif isinstance(regulation, CsvRegulation):
                # if regulation.pos_list == None:
                #     regulation.get_pos_list()

                s_class = regulation.target_class
                targets = scene.entities_of_type(s_class)

                for target in targets:
                    regulation.exert(target)

    @abstractmethod
    def zero_velocity(self):
        pass

    @abstractmethod
    def zero_angular_velocity(self):
        pass
