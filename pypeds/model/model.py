from abc import ABC, abstractmethod


class Model(ABC):

    def __init__(self, time_per_step, regulations=None):
        self.time_per_step = time_per_step
        self.regulations = regulations or []

    def step_next(self, scene):
        """ Define how will the model controls each entity's movement (or other changes in their attributes)

        :param scene:
        :return:
        """
        for regulation in self.regulations:
            # get interact classes
            s_class = regulation.source_class
            t_class = regulation.target_class

            # select interact entities
            sources = scene.entities_of_type(s_class)

            # exert
            for source in sources:
                # select affected entities in view
                targets_in_view = scene.entities_of_type_in_region(t_class, source.view)

                # let source exert affection on targets in view
                regulation.exert(source, targets_in_view)


    @abstractmethod
    def zero_velocity(self):
        pass

    @abstractmethod
    def zero_angular_velocity(self):
        pass
