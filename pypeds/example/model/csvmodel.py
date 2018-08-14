from pypeds.model.model import *
from pypeds.example.model.regulation import *
from pypeds.shape2d import Vector2D
import csv


class CSVModel(Model):
    def __init__(self, csv):
        super(CSVModel, self).__init__()
        self.regulations = []
        self.regulations.append(CsvRegulation(self, csv))

    def zero_angular_velocity(self):
        return 0

    def zero_velocity(self):
        return Vector2D(0, 0)
