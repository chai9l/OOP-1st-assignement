import functools
import sys
import json
import csv

from myCall import *
from myElevator import *
from myBuilding import *
import myCalls
import myElevator


class ElevatorAlgo:

    # def __init__(self, mb: myBuilding):
    #     self.building = mb
    #     self.calls = None

    def load_buildings(self, file_name) -> myBuilding:
        try:
            with open(file_name, 'r') as j_file:
                json_arr = json.load(j_file)
                b = myBuilding(json_arr.get("_minFloor"), json_arr.get("_maxFloor"), json_arr.get("_elevators"))
        except IOError:
            print("Error")

        return b

    def load_calls(self, file_name) -> []:
        ret = []
        try:
            with open(file_name, 'r') as csv_reader:
                self.calls = list(csv.reader(csv_reader))
                for i in self.calls:
                    call = myCall(i[1], i[2], i[3], i[5])
                    ret.append(call)
                return ret

        except IOError:
            return "Error"

    def allocate_elevators(self, b: str, c: str) -> bool:
        algo = ElevatorAlgo()
        building = algo.load_buildings(b)
        calls = algo.load_calls(c)

        return False


algo = ElevatorAlgo()
building = algo.load_buildings('Ex1_Buildings\\B1.json')
calls = algo.load_calls('Ex1_Calls\\Calls_a.csv')

for i in building.elevators:
    print(i)

for x in calls:
    print(x)
