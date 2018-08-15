from pypeds.shape2d import *
from pypeds.example.entity import *
from pypeds.gui.drawer.shape_drawer import *
import random


##TODO the generator of the entity shaped like rectangle has not been finished

class Generator(object):
    """
    Generator(.....).gird_generate()
    Generator(.....).random_generator()
    the Generator which adds the entities in the entitiesPool
    """

    def __init__(self, scene):
        self.last_time_generate = []
        self.scene = scene

    def grid_generate(self, scene, region_shape, entity, shape, radius, length, width, number, a, b, angle, interval):
        """

        :return: the ped enetities generated in the grid way and the ped_initial_pos with the entities' generated position
        """
        if entity == "Ped": entity = Pedestrian
        if entity == "Wall": entity = Wall
        if entity == "Safe-Region": entity = SafetyRegion

        if shape == "Circle" and number * radius ** 2 > region_shape.area() or \
                shape == "Box" and number * width * length > region_shape.area() or \
                shape == "Ellipse" and number * a * b * 4 > region_shape.area():
            print("generator deny")

        self.last_time_generate = []

        if shape == "Box":
            count_number = 0
            number_x = int(region_shape.length / (interval + length))
            number_y = int(region_shape.width / (interval + width))
            for m in range(0, number_y):
                for n in range(0, number_x):
                    generate_entity = entity(
                        Box2D(center=Point2D(region_shape.x_min + n * (interval + length / 2) + length / 2,
                                             region_shape.y_min + m * (interval + width / 2) + width / 2),
                              length=length, width=width))
                    scene.add_entity(generate_entity)
                    self.last_time_generate.append(generate_entity)
                    count_number += 1
                    if count_number == number:
                        return

        if shape == 'Circle':
            count_number = 0
            number_x = int(region_shape.length / (interval + radius * 2))
            number_y = int(region_shape.width / (interval + radius * 2))
            for m in range(0, number_y):
                for n in range(0, number_x):
                    generate_entity = entity(
                        Circle2D(center=Point2D(region_shape.x_min + n * (interval + radius) + radius,
                                                region_shape.y_min + m * (interval + radius) + radius),
                                 radius=radius))
                    scene.add_entity(generate_entity)
                    self.last_time_generate.append(generate_entity)

                    count_number += 1
                    if count_number == number:
                        return

        if shape == "Ellipse":
            if entity==Pedestrian: entity=RotatePedestrian
            count_number = 0
            number_x = int(region_shape.length / (interval + 2 * a * math.cos(angle)))
            number_y = int(region_shape.width / (interval + 2 * a * math.sin(angle)))
            for m in range(0, number_y):
                for n in range(0, number_x):
                    generate_entity = entity(
                        Ellipse2D(center=Point2D(
                            region_shape.x_min + n * (interval + 2 * abs(a * math.cos(angle))) + abs(a * math.cos(angle)),
                            region_shape.y_min + m * (interval + 2 * abs(a * math.sin(angle))) + abs(a * math.sin(angle))),
                            a=a, b=b, angle=angle))
                    scene.add_entity(generate_entity)
                    self.last_time_generate.append(generate_entity)
                    count_number += 1
                    if count_number == number:
                        return

    def random_generate(self, scene, region_shape, entity, shape, radius, length, width, number, a, b, angle):
        """

        :return:the ped entities generated in the random way and the ped_initial_pos with the entities' generated position
        """
        randomPool = []

        if entity == "Ped": entity = Pedestrian
        if entity == "Wall": entity = Wall
        if entity == "Safe-Region": entity = SafetyRegion

        if shape == "Circle" and number * radius ** 2 > region_shape.area() or \
                shape == "Box" and number * width * length > region_shape.area() or \
                shape == "Ellipse" and number * a * b * 4 > region_shape.area():
            print("generator deny")

        self.last_time_generate = []

        if shape == "Circle":

            region_x = [region_shape.center.x - region_shape.length / 2 + radius,
                        region_shape.center.x + region_shape.length / 2 - radius]
            region_y = [region_shape.center.y - region_shape.width / 2 + radius,
                        region_shape.center.y + region_shape.width / 2 - radius]
            random_x = [random.uniform(region_x[0], region_x[1]) for _ in range(number)]
            random_y = [random.uniform(region_y[0], region_y[1]) for _ in range(number)]

            for n in range(0, number):
                randomPool.append(entity(Circle2D(center=Point2D(random_x[n], random_y[n]), radius=radius)))
            for index in randomPool:
                for member in randomPool:
                    if index == member:
                        continue
                    if not index == member and DistanceCalculator.distance(index.shape, member.shape)[0] < 0:
                        randomPool.remove(member)
            for i in randomPool:
                scene.add_entity(i)
                self.last_time_generate.append(i)

        if shape == "Box":

            region_x = [region_shape.center.x - region_shape.length / 2 + length / 2,
                        region_shape.center.x + region_shape.length / 2 - length / 2]
            region_y = [region_shape.center.y - region_shape.width / 2 + width / 2,
                        region_shape.center.y + region_shape.width / 2 - width / 2]
            random_x = [random.uniform(region_x[0], region_x[1]) for _ in range(number)]
            random_y = [random.uniform(region_y[0], region_y[1]) for _ in range(number)]

            for n in range(0, number):
                randomPool.append(entity(Box2D(center=Point2D(random_x[n], random_y[n]), length=length, width=width)))
            for index in randomPool:
                for member in randomPool:
                    if index == member:
                        continue
                    if not index == member and DistanceCalculator.distance(index.shape, member.shape)[0] < 0:
                        randomPool.remove(member)
            for i in randomPool:
                scene.add_entity(i)
                self.last_time_generate.append(i)

        if shape == "Ellipse":
            if entity==Pedestrian: entity=RotatePedestrian
            region_x = [region_shape.center.x - region_shape.length / 2 + a * math.cos(angle),
                        region_shape.center.x + region_shape.length / 2 - a * math.cos(angle)]
            region_y = [region_shape.center.y - region_shape.width / 2 + a * math.sin(angle),
                        region_shape.center.y + region_shape.width / 2 - a * math.sin(angle)]
            random_x = [random.uniform(region_x[0], region_x[1]) for _ in range(number)]
            random_y = [random.uniform(region_y[0], region_y[1]) for _ in range(number)]

            for n in range(0, number):
                randomPool.append(entity(Ellipse2D(center=Point2D(random_x[n], random_y[n]), a=a, b=b, angle=angle)))
            for index in randomPool:
                for member in randomPool:
                    if index == member:
                        continue
                    if not index == member and DistanceCalculator.distance(index.shape, member.shape)[0] < 0:
                        randomPool.remove(member)
            for i in randomPool:
                scene.add_entity(i)
                self.last_time_generate.append(i)

    def common_generate(self, scene, entity, shape, center_x, center_y, radius, length, width, a, b, angle, data_list):
        """

        :return: the item entities generated in the random way and the ped_initial_pos with the entities' generated position
        """

        if entity == "Ped": entity = Pedestrian
        if entity == "Wall": entity = Wall
        if entity == "Safe-Region": entity = SafetyRegion
        if entity == "RecordPed": entity = RecordPed

        self.last_time_generate = []

        if shape == "Circle":
            generate_entity = entity(Circle2D(center=Point2D(center_x*50, center_y*50), radius=radius))
            if entity == RecordPed:
                generate_entity.data_list = data_list
            scene.add_entity(generate_entity)
            self.last_time_generate.append(generate_entity)

        if shape == "Box":
            generate_entity = entity((Box2D(center=Point2D(center_x, center_y), length=length, width=width)))
            scene.add_entity(generate_entity)
            self.last_time_generate.append(generate_entity)

        if shape == "Ellispse":
            if entity==Pedestrian: entity=RotatePedestrian
            generate_entity = entity(Ellipse2D(center=Point2D(center_x, center_y), a=a, b=b, angle=angle))
            scene.add_entity(generate_entity)
            self.last_time_generate.append(generate_entity)
