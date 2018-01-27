from pypeds.scene import *
from pypeds.entity import *
from pypeds.shape import *

scene = Scene()
scene.add_entity(Agent(Circle2D(center=(1, 2), radius=3)))
print(scene.agents)