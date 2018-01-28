from abc import ABC, abstractmethod

__all__ = ['Force', 'PsychologicalForce', 'BodyForce']


class Force(ABC):
    def __init__(self, class_a, class_b, model = None):
        self.class_a, self.class_b = class_a, class_b
        self.model = model

    def has_force(self, source, affected) -> bool:
        """
        :return: Return if source and affected has force to each other, based on previously defined class_a and class_b
        """
        return isinstance(source, self.class_a) and isinstance(affected, self.class_b)

    @abstractmethod
    def exert(self, source, affected):
        """At here, each successor force should define how 'source' entity put its force on 'affected'

        :param source: The source of force
        :param affected: The affected entity
        :return:
        """
        pass


class PsychologicalForce(Force):
    def __init__(self, class_a, class_b):
        super().__init__(class_a, class_b)

    def exert(self, source, affected):
        if not self.has_force(source, affected):
            return

        pass


class BodyForce(Force):
    def __init__(self, class_a, class_b):
        super().__init__(class_a, class_b)

    def exert(self, source, affected):
        if not self.has_force(source, affected):
            return

        pass