from abc import ABC, abstractmethod


class Regulation(ABC):
    def __init__(self, model=None):
        self.model = model

    @abstractmethod
    def exert(self, source, affected):
        """ At here, each successor force should define how 'source' entity puts its force on 'affected' (which could
         be one or many)

        And we let affection exert directly on the affected entity
        :param source: The source of force
        :param affected: The affected entity
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
    def affected_class(self):
        try:
            return self._affected_class
        except AttributeError:
            raise NotImplementedError(
                "Subclasses of Regulation must set an instance attribute "
                "self._affected_class in it's __init__ method")

    @affected_class.setter
    def affected_class(self, affected_class):
        self._affected_class = affected_class

