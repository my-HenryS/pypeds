from pypeds.gui.panel import *
from pypeds.example.strategy import *

scene = Scene()
scene.model = SFModel(0.004)
scene.add_entity(Wall(Box2D(Point2D(18, 25), 1, 10)))
scene.add_entity(Wall(Box2D(Point2D(28, 25), 1, 10)))
scene.add_entity(Wall(Box2D(Point2D(23, 29.5), 9, 1)))
scene.add_entity(Wall(Box2D(Point2D(20.5, 20.5), 4, 1)))
scene.add_entity(Wall(Box2D(Point2D(25.5, 20.5), 4, 1)))

scene.pack()
print(scene.bound)
path = GridPath.create_path(scene, Circle2D(Point2D(0,0), 0.486/2), Point2D(30,30))
print(path.next_step(Point2D(26,26.2)))