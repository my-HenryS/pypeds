

class EntityPool(object):

    def __init__(self, entities=None):
        self.__entities = entities or []

    def select_all(self, q_type) -> iter:
        """ Get all entities that are instances of qType (or any of its super classes)

        :param q_type: the query type
        :return: iterator that contains all the satisfied instances
        """
        return filter(lambda x: isinstance(x, q_type), self.__entities).__iter__() if len(self.__entities) is not 0 \
            else [].__iter__()

    def select_all_within(self, region) -> iter:
        """ Get all entities whose shapes are intersected with region

        :param region: the query region
        :return: iterator that contains all the satisfied instances
        """
        return filter(lambda x: region.intersects(x.shape), self.__entities).__iter__() \
            if len(self.__entities) is not 0 else [].__iter__()

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