from pypeds.model.regulation import Regulation
from pypeds.example.entity import *
from pypeds.model.affection import *
import csv
import time


class CsvRegulation():

    def __init__(self, model, csv):
        super(CsvRegulation, self).__init__()
        self.target_class = Movable
        self.model = model
        self.csv = csv
        self.pos_list = None

    def exert(self, entity):
        if len(entity.data_list) != 1:
            affection = Affection(a_type="Csv", value=Point2D(50*float(entity.data_list[0].split(",")[0]),50*float(entity.data_list[0].split(",")[1])))
            del entity.data_list[0]
        else:
            affection = Affection(a_type="CSV",value=Point2D(50*float(entity.data_list[0].split(",")[0]),50*float(entity.data_list[0].split(",")[1])))
        time.sleep(0.001)

        entity.affected(affection)

    def get_pos_list(self):
        pos_list = []
        temp = []
        csv_reader = csv.reader(open(self.csv, "r", newline=""))
        for row in csv_reader:
            for index in row:
                temp.append(index[1:-1])
            pos_list.append(temp)
            temp = []

        self.pos_list = pos_list
