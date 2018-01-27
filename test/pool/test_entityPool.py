from unittest import TestCase

from pypeds.entity import *
from pypeds.pool import *
from pypeds.shape import *


class TestEntityPool(TestCase):
    def setUp(self):
        self.testAgent1 = Agent(Circle2D())
        self.entities = EntityPool([Agent()])

    def test_get(self):
        self.assertEqual()
