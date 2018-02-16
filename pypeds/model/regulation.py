from abc import ABC, abstractmethod


class Regulation(ABC):
    def __init__(self, model=None):
        self.model = model

    @abstractmethod
    def exert(self, source, targets):
        """ At here, each successor force should define how 'source' entity puts its force on each 'target' (which should be
         iterable)

        And we let affection exert directly on the affected entity by calling its affected
        :param source: The source entity of force
        :param targets: The target entities
        :return:
        """
        pass

    @property
    def source_class(self):
        try:
            return self._source_class
        except AttributeError:
            raise NotImplementedError(
                "Subclasses of Regulation must set an instance attribute "
                "self._source_class in it's __init__ method")

    @source_class.setter
    def source_class(self, source_class):
        self._source_class = source_class

    @property
    def target_class(self):
        try:
            return self._target_class
        except AttributeError:
            raise NotImplementedError(
                "Subclasses of Regulation must set an instance attribute "
                "self._target_class in it's __init__ method")

    @target_class.setter
    def target_class(self, target_class):
        self._target_class = target_class


class SingleTargetRegulation(Regulation):
    """
    Source entity in single target affection only affect on a single target each function call. It may have multiple targets
    to affect each time step.
    """
    def exert(self, source, targets):
        for target in targets:
            self.exert_single(source, target)

    @abstractmethod
    def exert_single(self, source, target):
        """ Define how source exert affection on single target

        :param source:
        :param target:
        :return:
        """
        pass


class SelfDrivenRegulation(ABC):
    """ Self driven regulation regulates how entities affect on themselves.

    """
    def __init__(self, model=None):
        self.model = model

    @abstractmethod
    def exert(self, entity):
        """ At here, each successor force should define how entities affect on themselves

        :param entity: The source entity of force
        :return:
        """
        pass

    @property
    def source_class(self):
        try:
            return self._source_class
        except AttributeError:
            raise NotImplementedError(
                "Subclasses of Regulation must set an instance attribute "
                "self._source_class in it's __init__ method")

    @source_class.setter
    def source_class(self, source_class):
        self._source_class = source_class