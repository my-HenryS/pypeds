from abc import ABC, abstractmethod
# TODO affected -> target


class Regulation(ABC):
    def __init__(self, model=None):
        self.model = model

    @abstractmethod
    def exert(self, source, target):
        """ At here, each successor force should define how 'source' entity puts its force on 'target' (which could
         be one or many)

        And we let affection exert directly on the affected entity
        :param source: The source of force
        :param target: The target entity or entities
        :return:
        """
        pass

    @property
    def is_multiple(self):
        try:
            return self._is_multiple
        except AttributeError:
            raise NotImplementedError(
                "Subclasses of Regulation must set an instance attribute "
                "self._is_multiple in it's __init__ method")

    @is_multiple.setter
    def is_multiple(self, is_multiple):
        self._is_multiple = is_multiple

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

