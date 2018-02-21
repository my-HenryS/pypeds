from pypeds.example.model.sfmodel import SFModel, Pedestrian
from pypeds.scene import Scene
from pypeds.shape2d import Circle2D, Point2D


class A(object):

    def func(self):
        print(type(self))

class B(A):
    pass


a = B()
a.func()

scene = Scene()
model = SFModel(0.004)
scene.model = model
ped = Pedestrian(Circle2D(center=Point2D(4, 11), radius=5))
scene.add_entity(ped)
scene.add_entity(Pedestrian(Circle2D(center=Point2D(11, 11), radius=5)))

peds = scene.entities_of_type(Pedestrian)
for agent in peds:
    print(agent)

scene.remove_entity(ped)

for agent in peds:
    print(agent)