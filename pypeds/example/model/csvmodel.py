from pypeds.model.model import *
from pypeds.example.model.regulation import *
from pypeds.shape2d import Vector2D
import csv
from pypeds.generator import *


class CSVModel(Model):
    def __init__(self, time_per_step, csv, scene):
        super(CSVModel, self).__init__(time_per_step)
        self.regulations = []
        self.regulations.append(CsvRegulation(self, csv))
        self.scene = scene

    def on_add(self):
        self.regulations[0].get_pos_list()
        for index in self.regulations[0].pos_list:
            self.scene.generator.common_generate(scene=self.scene, entity="RecordPed",shape= "Circle", center_x=float(index[0].split(",")[0]),center_y= float(index[0].split(",")[1]),
                                                 radius=2,length= 5,width= 5,a=5,b= 5, angle=5,data_list=index)


    def zero_angular_velocity(self):
        return 0

    def zero_velocity(self):
        return Vector2D(0, 0)
