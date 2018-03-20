from pypeds.shape2d import *
from pypeds.example.entity import *
from pypeds.gui.drawer.shape_drawer import *
import random


##TODO the generator of the enetiy shaped like rectangle has not been finished

class Generator(object):
    """
    Generator(.....).gird_generate()
    Generator(.....).random_generator()
    the Generator which adds the entities in the entitiesPool
    """

    def __init__(self, window):
        self.window = window

    def grid_generate(self, scene, region_shape, entity, shape, number=0, interval=10):
        """

        :return: the ped enetities generated in the grid way and the ped_initial_pos with the entities' generated position
        """

        radius = float(self.window.lineEdit_43.text())
        length = float(self.window.lineEdit_44.text())
        width = float(self.window.lineEdit_45.text())

        if entity == "Ped": entity = Pedestrian
        if entity == "Wall": entity = Wall
        if entity == "Safe-Region": entity = SafetyRegion

        if shape == "Circle" and number * radius ** 2 > region_shape.area() or shape == "Box" and number * width * length > region_shape.area():
            print("generator deny")

        count_number = 0
        number_x = int(region_shape.length / (interval + length * 2))
        number_y = int(region_shape.width / (interval + width * 2))
        for m in range(0, number_y):
            for n in range(0, number_x):
                if shape == "Box":
                    scene.add_entity(entity(
                        Box2D(center=Point2D(region_shape.e_left + n * (interval + length / 2) + length / 2,
                                         region_shape.e_down + m * (interval + width / 2) + width / 2),
                          length=length, width=width)))
                elif shape == 'Circle':
                    scene.add_entity(entity(
                        Circle2D(center=Point2D(region_shape.e_left + n * (interval + radius) + radius,
                                                region_shape.e_down + m * (interval + radius) + radius),
                                 radius=radius)))

                count_number += 1
                if count_number == number:
                    return

    def random_generate(self, scene, region_shape, entity, shape, number=0, radius=0.243, interval=10):
        """

        :return:the ped entities generated in the random way and the ped_initial_pos with the entities' generated position
        """
        randomPool = []

        radius = float(self.window.lineEdit_46.text())
        length = float(self.window.lineEdit_47.text())
        width = float(self.window.lineEdit_48.text())

        if entity == "Ped": entity = Pedestrian
        if entity == "Wall": entity = Wall
        if entity == "Safe-Region": entity = SafetyRegion

        if shape == "Circle" and number * radius ** 2 > region_shape.area() or shape == "Box" and number * width * length > region_shape.area():
            print("generator deny")

        region_x = [region_shape.center.x - region_shape.length / 2 + radius,
                    region_shape.center.x + region_shape.length / 2 - radius]
        region_y = [region_shape.center.y - region_shape.width / 2 + radius,
                    region_shape.center.y + region_shape.width / 2 - radius]
        random_x = [random.uniform(region_x[0], region_x[1]) for _ in range(number)]
        random_y = [random.uniform(region_y[0], region_y[1]) for _ in range(number)]

        if shape == "Circle":
            for n in range(0, number):
                randomPool.append(entity(Circle2D(Point2D(random_x[n], random_y[n]), radius)))
            for index in randomPool:
                for member in randomPool:
                    if index == member:
                        continue
                    if not index == number and DistanceCalculator.distance(index.shape, member.shape)[0] < 0:
                        randomPool.remove(member)
            for i in randomPool:
                scene.add_entity(i)

        if shape == "Box":
            for n in range(0, number):
                randomPool.append(entity(Box2D(Point2D(random_x[n], random_y[n]), length, width)))
            for index in randomPool:
                for member in randomPool:
                    if index == member:
                        continue
                    if not index == member and DistanceCalculator.distance(index.shape, member.shape)[0] < 0:
                        randomPool.remove(entity)
            for i in randomPool:
                scene.add_entity(i)

    def common_generate(self, scene, entity, shape):
        """

        :return: the item entities generated in the random way and the ped_initial_pos with the entities' generated position
        """

        if not scene.getName() in self.initial_pos:
            self.initial_pos[scene.getName()] = []

        center_x = float(self.window.lineEdit_57.text())
        center_y = float(self.window.lineEdit_58.text())
        radius = float(self.window.lineEdit_49.text())
        length = float(self.window.lineEdit_50.text())
        width = float(self.window.lineEdit_51.text)

        if entity == "Ped": entity = Pedestrian
        if entity == "Wall": entity = Wall
        if entity == "Safe-Region": entity = SafetyRegion

        if shape == "Circle":
            scene.add_entity(entity(Circle2D(Point2D(center_x, center_y), radius)))

        if shape == "Box":
            scene.add_entity(entity(Box2D(Point2D(center_x, center_y), length, width)))
