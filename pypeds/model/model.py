from abc import ABC, abstractmethod


class Model(ABC):

    def __init__(self, time_per_step, regulations = None):
        self.time_per_step = time_per_step
        self.regulations = regulations

    def step_next(self, entities):
        """ Define how will the model controls each entity's movement (or other changes in their attributes)

        :param entities:
        :return:
        """
        for regulation in self.regulations:
            # get interact classes
            s_class = regulation.source_class
            a_class = regulation.affected_class

            # select interact entities
            sources = entities.select_all(s_class)
            affecteds = entities.select_all(a_class)

            # exert
            for source in sources:
                # select affected entities in view
                affecteds_in_view = affecteds.select_all_within(source.view)

                # decide whether to affect together or not
                if regulation.is_multiple:
                    regulation.exert(source, affecteds_in_view)
                else:
                    for affected in affecteds_in_view:
                        regulation.exert(source, affected)

    @abstractmethod
    def zero_velocity(self):
        pass

    @abstractmethod
    def zero_angular_velocity(self):
        pass
