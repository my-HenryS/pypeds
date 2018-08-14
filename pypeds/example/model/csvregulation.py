from pypeds.model.regulation import Regulation
from pypeds.example.entity import *


class CsvRegulation():

    def __init__(self, model, csv):
        super(CsvRegulation, self).__init__()
        self.target_class = Movable
        self.model = model
        self.csv = csv
        self.pos_list = None

    def exert(self, entity):
        # affection =
        entity.affected(affection)
        pass

    def get_pos_list(self):
        csv_reader = open(self.csv, "r", newline="")
        pass