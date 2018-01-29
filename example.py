from pypeds.scene import *
from pypeds.entity import *
from pypeds.shape import *
from pypeds.gui.panel import *

scene = Scene()
scene.add_entity(Agent(Circle2D(center=(4, 4), radius=5)))

p = Panel("Simulation")

scene.add_listener(p)
while True:
    scene.step_next()
    p.window.update()
