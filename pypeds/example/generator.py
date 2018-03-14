from pypeds.shape2d import *
from pypeds.example.entity import *
from pypeds.gui.drawer.shape_drawer import *
import random


##TODO the generator of the enetiy shaped like rectangle has not been finished

class Generator():
    """
    Generator(.....).gird_generate()
    Generator(.....).random_generator()
    the Generator which adds the entities in the entitiesPool
    """

    def __init__(self, scene):
        """

        :param scene: the scene of generator
        """
        self.scene = scene

    def grid_generate(self, region_shape, number=0, radius=0.243, interval=10):
        """

        :return: the enetities generated in the grid way
        """
        if number * radius ** 2 > region_shape.area():
            print("generator deny")
        count_number = 0
        number_x = int(region_shape.length / (interval + radius * 2))
        number_y = int(region_shape.width / (2 * radius))
        for m in range(0, number_y):
            for n in range(0, number_x):
                self.scene.add_entity(Pedestrian(
                    self.scene.pedestrain_shape(Point2D(region_shape.e_left + n * interval + radius,
                                                        region_shape.e_down + m * interval + radius),
                                                radius)))
                # Circle2DDrawer.draw(self.scene.pedestrain_shape(Point2D(region_shape.e_left + n * interval + radius,
                #                                                         region_shape.e_down + m * interval + radius),
                #                                                 radius))
                count_number += 1
                if count_number == number:
                    return

    def random_generate(self, region_shape, number=0, radius=0.243, interval=10):
        """

        :return:the entities generated in the random way
        """
        region_x = [region_shape.center.x - region_shape.length / 2 + radius,
                    region_shape.center.x + region_shape.length / 2 - radius]
        region_y = [region_shape.center.y - region_shape.width / 2 + radius,
                    region_shape.center.y + region_shape.width / 2 - radius]
        random_x = [random.uniform(region_x[0], region_x[1]) for _ in range(number)]
        random_y = [random.uniform(region_y[0], region_y[1]) for _ in range(number)]
        for n in range(0, number):
            self.scene.add_entity(
                Pedestrian(self.scene.pedestrain_shape(Point2D(random_x[n], random_y[n]), radius)))
        for index in iter(self.scene._entities):
            for member in iter(self.scene._entities):
                if index == member:
                    continue
                if not index == member and DistanceCalculator.distance(index.shape, member.shape)[0] < 0:
                    self.scene.remove_entity(member)

    def item_generate(self, entity, region_shape):
        self.scene.add_entity(entity(region_shape))

    # def generate_show(self):
    #     for entity in iter(self.scene._entities):
    #         entity.drawer.draw

