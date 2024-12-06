import os
import manager_data
from pathlib import Path

def get_season_data_from(path):
    all_gw_data = list()
    for file in os.listdir(path):
        if os.fsdecode(file).endswith(".score"):
            name = Path(file).stem
            gw_data = get_manager_data_from(path + "\\" + file)
            all_gw_data.append(manager_data.manager_data(name, gw_data))
    return all_gw_data

def get_manager_data_from(path):
    gw_data = list()
    for line in open(path):
        gw_data.append(float(line.rstrip()))
    return gw_data
    
class data_reader:
    def __init__(self, year):
        print("Initializing data reader for year: " + year)
        self.path_to_data = os.getcwd() + "\\data\\seasons\\" + year
        self.season_data = get_season_data_from(self.path_to_data)
    
    def get_data(self):
        return self.season_data