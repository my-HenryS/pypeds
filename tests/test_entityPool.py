from unittest import TestCase

from pypeds.entity import *
from pypeds.pool import *
from pypeds.scene import *


class TestEntityPool(TestCase):
    def setUp(self):
        self.agent1 = Agent(1)
        self.agent2 = Agent(2)
        self.dummy1 = Dummy(1)
        self.entities = EntityPool([self.agent1, self.agent2])

    def test_select(self):
        iter_ = self.entities.select(Agent)
        self.assertEqual(self.agent1, iter_.__next__())
        self.assertEqual(self.agent2, iter_.__next__())

    def test_add(self):
        self.entities.add(self.dummy1)
        iter_ = self.entities.select(Dummy)
        self.assertEqual(self.dummy1, iter_.__next__())

    def test_remove(self):
        self.entities.remove(self.agent1)
        iter_ = self.entities.select(Agent)
        self.assertEqual(self.agent2, iter_.__next__())

