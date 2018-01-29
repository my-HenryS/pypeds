__all__ = ['EntityPool']


class EntityPool(object):

    def __init__(self, entities):
        self.__entities = entities or []

    def select(self, qType) -> iter:
        """ Get all entities that are instances of qType (or any of its super classes)

        :param qType: the query type
        :return: iterator that contains all the satisfied instances
        """
        return filter(lambda x: isinstance(x, qType), self.__entities).__iter__() if len(self.__entities) is not 0 \
            else [].__iter__()

    def add(self, new_entity):
        """ Add 'new_entity' into __entities

        :param new_entity: entity to be added
        """
        self.__entities.append(new_entity)

    def remove(self, entity):
        """ Remove the first-found 'entity' from __entities

        :param entity: entity to be removed
        """
        self.__entities.remove(entity)

    def __str__(self):
        string = ""
        for entity in self.__entities:
            string += str(entity)
        return string

    def __iter__(self):
        return self.__entities.__iter__()