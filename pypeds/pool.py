

class EntityPool(object):

    def __init__(self, entities=None):
        self.__entities = entities or []

    def select_by_type(self, q_type):
        """ Get all entities who are instances of qType (or any of its super classes)

        :param q_type: the query type
        :return: iterator that contains all the satisfied instances
        """
        return filter(lambda x: isinstance(x, q_type), self.__entities) if len(self.__entities) is not 0 \
            else []

    def select_by_region(self, region):
        """ Get all entities whose shapes are intersected with region

        :param region: the query region
        :return: iterator that contains all the satisfied instances
        """
        return filter(lambda x: region.intersects(x.shape), self.__entities) \
            if len(self.__entities) is not 0 else [].__iter__()

    def select_type_in_region(self, q_type, region):
        """ Get all entities who are instances of qType and whose shapes are intersected with region

        :param region: the query region
        :param q_type: the query type
        :return: iterator that contains all the satisfied instances
        """
        return filter(lambda x: isinstance(x, q_type) and region.intersects(x.shape), self.__entities) \
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

    def __len__(self):
        len = 0
        for entity in self.__entities:
            len += 1
        return len