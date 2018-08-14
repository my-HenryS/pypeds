from pypeds.model.regulation import Regulation
from pypeds.example.entity import *
from pypeds.model.affection import *
import csv

class CsvRegulation():

    def __init__(self, model, csv):
        super(CsvRegulation, self).__init__()
        self.target_class = Movable
        self.model = model
        self.csv = csv
        self.pos_list = None


    def exert(self, entity):

        # affection = Affection(a_type="Csv",value=)
        # entity.affected(affection)
        pass

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