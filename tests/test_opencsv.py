from unittest import TestCase

from pypeds.example.model.csvregulation import *
from pypeds.example.model.csvmodel import *

if __name__ == "__main__":
    csv_model = CSVModel(0.004, "/home/hdl/PycharmProjects/pypeds/pypeds/example/resources/ffffffffffff.csv")
    csv_model.regulations[0].get_pos_list()
