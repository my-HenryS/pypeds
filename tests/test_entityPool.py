from unittest import TestCase

from pypeds.pool import *
from pypeds.scene import *
from pypeds.entity import Movable
from pypeds.example.entity import Pedestrian


class TestEntityPool(TestCase):
    def setUp(self):
        self.agent1 = Movable(1)
        self.agent2 = Movable(2)
        self.peds1 = Pedestrian(1)
        self.entities = EntityPool([self.agent1, self.agent2])

    def test_select(self):
        iter_ = self.entities.select_all(Movable)
        self.assertEqual(self.agent1, iter_.__next__())
        self.assertEqual(self.agent2, iter_.__next__())

    def test_add(self):
        self.entities.add(self.peds1)
        iter_ = self.entities.select_all(Pedestrian)
        self.assertEqual(self.peds1, iter_.__next__())

    def test_remove(self):
        self.entities.remove(self.agent1)
        iter_ = self.entities.select_all(Movable)
        self.assertEqual(self.agent2, iter_.__next__())

